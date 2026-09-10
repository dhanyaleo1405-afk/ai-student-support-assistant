
---

# 3. `tools.py`

This file contains the tools used by the agents.

```python
from typing import Dict


# =========================================
# DSA TOOL
# =========================================

def get_dsa_questions(
    query: str
) -> Dict:

    context = """

DSA Practice Bank

1. Two Sum
   Topic: Hash Map
   Difficulty: Easy

2. Valid Parentheses
   Topic: Stack
   Difficulty: Easy

3. Best Time to Buy and Sell Stock
   Topic: Array
   Difficulty: Easy

4. Longest Substring Without Repeating Characters
   Topic: Sliding Window
   Difficulty: Medium

5. Merge Intervals
   Topic: Sorting
   Difficulty: Medium

6. Reverse Linked List
   Topic: Linked List
   Difficulty: Easy

7. Binary Search
   Topic: Searching
   Difficulty: Easy

8. Number of Islands
   Topic: Graph / BFS / DFS
   Difficulty: Medium

9. Maximum Subarray
   Topic: Kadane's Algorithm
   Difficulty: Medium

10. Longest Palindromic Substring
    Topic: String
    Difficulty: Medium

"""


    return {

        "context": context,

        "sources": [
            "Local DSA practice bank"
        ]
    }


# =========================================
# PLACEMENT TOOL
# =========================================

def get_placement_plan(
    query: str,
    student: Dict
) -> Dict:


    context = """

PLACEMENT PREPARATION FRAMEWORK

Programming:

- Python
- Java
- C++
- OOP
- Problem solving


DSA:

- Arrays
- Strings
- Hashing
- Linked Lists
- Stack
- Queue
- Trees
- Graphs
- Searching
- Sorting


SQL:

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- JOIN
- Subqueries
- Window Functions


APTITUDE:

- Percentages
- Ratios
- Averages
- Profit and Loss
- Time and Work
- Probability
- Logical Reasoning


CORE CS:

- DBMS
- Operating Systems
- Computer Networks
- OOP


INTERVIEW:

- Self introduction
- Project explanation
- Coding explanation
- Resume discussion
- HR questions


SUGGESTED WEEKLY PLAN:

Monday-Friday:

60 min → DSA

45 min → SQL / CS

30 min → Aptitude


Weekend:

Mock test

Project improvement

Resume improvement

"""


    return {

        "context": context,

        "sources": [
            "Local placement preparation framework"
        ]
    }


# =========================================
# PROJECT TOOL
# =========================================

def get_project_ideas(
    query: str
) -> Dict:


    context = """

AI / STUDENT PROJECT IDEAS

1. AI Student Support Assistant

Technology:

Python
Ollama
Streamlit
SQLite


2. Placement Preparation Planner

Technology:

Python
SQLite
Streamlit


3. College FAQ Assistant

Technology:

Ollama
RAG
Python
Streamlit


4. Student Attendance Analytics

Technology:

Python
Pandas
Power BI


5. Resume Skill Gap Analyzer

Technology:

Python
Ollama
Rule-based matching


PROJECT DOCUMENTATION

A good project should contain:

Problem Statement

Objectives

Existing System

Proposed System

Architecture

Agents

Tools

Technology Stack

Implementation

Testing

Results

Advantages

Limitations

Future Enhancement

Conclusion

"""


    return {

        "context": context,

        "sources": [
            "Local project idea bank"
        ]
    }


# =========================================
# CAREER TOOL
# =========================================

def get_career_advice(
    query: str,
    student: Dict
) -> Dict:


    context = """

CAREER FRAMEWORK


Software Engineer:

Programming

DSA

OOP

DBMS

Operating Systems

Computer Networks


Data Analyst:

SQL

Excel

Power BI

Statistics

Python

Data Visualization


AI/ML Engineer:

Python

Machine Learning

Deep Learning

Statistics

Data Processing

Model Deployment


IMPORTANT:

Career recommendations should depend
on the student's interests, skills,
projects and target job.

Never guarantee a job or salary.

"""


    return {

        "context": context,

        "sources": [
            "Local career framework"
        ]
    }


# =========================================
# ACADEMIC TOOL
# =========================================

def get_academic_advice(
    query: str,
    student: Dict
) -> Dict:


    context = """

ACADEMIC STUDY FRAMEWORK


Step 1:

Understand the syllabus.


Step 2:

Divide the subject into concepts.


Step 3:

Learn one concept at a time.


Step 4:

Solve 3-5 questions.


Step 5:

Create short notes.


Step 6:

Revise using spaced repetition.


Step 7:

Maintain an error log.


BEFORE EXAM:

Prioritize:

- Syllabus
- Previous questions
- Important concepts
- Weak topics
- Revision


"""


    return {

        "context": context,

        "sources": [
            "Local academic study framework"
        ]
    }
