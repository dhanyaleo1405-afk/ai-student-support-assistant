import sqlite3
from pathlib import Path


# Database location
DB_PATH = Path(
    "data/student_support.db"
)


class StudentDatabase:

    def __init__(self):

        # Create data folder
        DB_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        # Connect SQLite
        self.conn = sqlite3.connect(

            DB_PATH,

            check_same_thread=False
        )


        # Create tables
        self._create_tables()


    # =====================================
    # CREATE DATABASE TABLE
    # =====================================

    def _create_tables(self):

        self.conn.execute("""

            CREATE TABLE IF NOT EXISTS students (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT NOT NULL,

                course TEXT,

                year TEXT,

                goal TEXT

            )

        """)


        self.conn.commit()


    # =====================================
    # SAVE STUDENT
    # =====================================

    def save_student(
        self,
        name,
        course,
        year,
        goal
    ):

        self.conn.execute(

            """

            INSERT INTO students
            (
                name,
                course,
                year,
                goal
            )

            VALUES (?, ?, ?, ?)

            """,

            (
                name,
                course,
                year,
                goal
            )
        )


        self.conn.commit()
