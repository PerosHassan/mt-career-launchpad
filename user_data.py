import sqlite3
from database import get_connection


# ============================================================
# SAVE USER PROFILE
# ============================================================

def save_profile(
    user_id,
    career_goal,
    skills,
    experience,
    education
):

    conn = get_connection()
    cursor = conn.cursor()


    # Check if profile already exists

    cursor.execute(
        """
        SELECT id 
        FROM profiles
        WHERE user_id=?
        """,
        (user_id,)
    )


    existing = cursor.fetchone()



    if existing:

        cursor.execute(
            """
            UPDATE profiles

            SET
            career_goal=?,
            skills=?,
            experience=?,
            education=?

            WHERE user_id=?

            """,
            (
                career_goal,
                skills,
                experience,
                education,
                user_id
            )
        )


    else:

        cursor.execute(
            """
            INSERT INTO profiles
            (
            user_id,
            career_goal,
            skills,
            experience,
            education
            )

            VALUES (?, ?, ?, ?, ?)

            """,
            (
                user_id,
                career_goal,
                skills,
                experience,
                education
            )
        )


    conn.commit()
    conn.close()



# ============================================================
# GET USER PROFILE
# ============================================================

def get_profile(user_id):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        career_goal,
        skills,
        experience,
        education

        FROM profiles

        WHERE user_id=?

        """,
        (user_id,)
    )


    profile = cursor.fetchone()


    conn.close()


    return profile



# ============================================================
# SAVE AI RESULT HISTORY
# ============================================================

def save_ai_history(
    user_id,
    task,
    input_text,
    ai_response
):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO ai_history
        (
        user_id,
        task,
        input_text,
        ai_response
        )

        VALUES (?, ?, ?, ?)

        """,
        (
            user_id,
            task,
            input_text,
            ai_response
        )
    )


    conn.commit()

    conn.close()



# ============================================================
# GET USER AI HISTORY
# ============================================================

def get_user_history(user_id):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        task,
        ai_response,
        created_at

        FROM ai_history

        WHERE user_id=?

        ORDER BY id DESC

        """,
        (user_id,)
    )


    history = cursor.fetchall()


    conn.close()


    return history
