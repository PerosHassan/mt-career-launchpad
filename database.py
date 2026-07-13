import sqlite3


DATABASE_NAME = "users.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    return conn



# ============================================================
# CREATE TABLES
# ============================================================

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()


    # ============================
    # USERS TABLE
    # ============================

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """
    )



    # ============================
    # USER PROFILE TABLE
    # ============================

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS profiles (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        career_goal TEXT,

        skills TEXT,

        experience TEXT,

        education TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


        FOREIGN KEY(user_id)
        REFERENCES users(id)

    )
    """
    )



    # ============================
    # AI HISTORY TABLE
    # ============================

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ai_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,


        user_id INTEGER NOT NULL,


        task TEXT NOT NULL,


        input_text TEXT,


        ai_response TEXT,


        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


        FOREIGN KEY(user_id)
        REFERENCES users(id)

    )
    """
    )



    conn.commit()

    conn.close()



# ============================================================
# INITIALIZE DATABASE
# ============================================================

create_tables()
