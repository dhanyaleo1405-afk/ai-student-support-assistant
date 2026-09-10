import streamlit as st
from agents import StudentSupportOrchestrator

st.set_page_config(
    page_title="AI Student Support Assistant",
    page_icon="🎓",
    layout="wide"
)


@st.cache_resource
def get_orchestrator():
    return StudentSupportOrchestrator()


orchestrator = get_orchestrator()

st.title("🎓 AI Student Support Assistant")
st.caption("Agentic AI + Ollama + SQLite")

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.header("👨‍🎓 Student Profile")

    name = st.text_input(
        "Student Name",
        value="Student"
    )

    course = st.text_input(
        "Course",
        value="B.E CSE - AI & ML"
    )

    year = st.text_input(
        "Year",
        value="Final Year"
    )

    goal = st.selectbox(
        "Current Goal",
        [
            "Placement",
            "Exam Preparation",
            "Project Development",
            "Data Analytics",
            "DSA",
            "General Study"
        ]
    )

    st.divider()

    st.subheader("⚡ Quick Actions")

    quick_questions = [
        "Create a 7-day placement study plan",
        "Give me 5 DSA interview questions",
        "Suggest an AI final year project",
        "How can I prepare for aptitude?"
    ]

    for question in quick_questions:

        if st.button(
            question,
            use_container_width=True
        ):
            st.session_state["quick_prompt"] = question


# -----------------------------
# CHAT HISTORY
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# USER INPUT
# -----------------------------

prompt = st.chat_input(
    "Ask your student support assistant..."
)


# Quick action input
if "quick_prompt" in st.session_state:

    prompt = st.session_state.pop(
        "quick_prompt"
    )


# -----------------------------
# PROCESS QUESTION
# -----------------------------

if prompt:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)


    # AI response
    with st.chat_message("assistant"):

        with st.spinner(
            "AI agents are thinking..."
        ):

            result = orchestrator.handle(

                user_query=prompt,

                student={
                    "name": name,
                    "course": course,
                    "year": year,
                    "goal": goal
                },

                history=st.session_state.messages[-8:]
            )

            answer = result["answer"]

            st.markdown(answer)


            # Show agent actions
            if result.get("actions"):

                with st.expander(
                    "🤖 Agent Actions"
                ):

                    for action in result["actions"]:

                        st.write(
                            "• " + action
                        )


            # Show sources
            if result.get("sources"):

                with st.expander(
                    "📚 Knowledge Sources"
                ):

                    for source in result["sources"]:

                        st.write(
                            "• " + source
                        )


    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
