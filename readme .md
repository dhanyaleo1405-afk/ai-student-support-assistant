# 🎓 AI Student Support Assistant using Agentic AI and Ollama

An Agentic AI based Student Support Assistant built using Python,
Streamlit, Ollama and SQLite.

## 🎯 Objective

The objective of this project is to develop an intelligent AI assistant
that can help students with:

- Academic preparation
- DSA practice
- Placement preparation
- Career guidance
- Project ideas
- Study planning

The system uses an agentic workflow to understand the student's request,
select the appropriate tool and generate a personalized response.

---

# 🤖 Agentic AI Architecture

Student
   |
   v
Streamlit Interface
   |
   v
Router Agent
   |
   +----------------+
   |       |        |
Academic Career    DSA
   |       |        |
Placement Project  General
   |
   v
Tool Agent
   |
   v
Local Knowledge
   |
   v
Ollama LLM
   |
   v
Final AI Response

---

# 🛠️ Technology Stack

- Python
- Streamlit
- Ollama
- Gemma 3
- SQLite
- Git
- GitHub

---

# 🤖 AI Model

This project uses Ollama to run a local Large Language Model.

Recommended model:

gemma3:4b

Install it using:

```bash
ollama pull gemma3:4b
