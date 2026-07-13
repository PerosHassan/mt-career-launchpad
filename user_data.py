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
    # ============================================================
# GET USER STATISTICS
# ============================================================

def get_user_stats(user_id):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT task, COUNT(*)

        FROM ai_history

        WHERE user_id=?

        GROUP BY task

        """,
        (user_id,)
    )


    results = cursor.fetchall()


    conn.close()


    stats = {

        "resume": 0,
        "career": 0,
        "cv": 0,
        "roadmap": 0,
        "interview": 0

    }


    for task, count in results:

        if task in stats:

            stats[task] = count


    return stats
    # ============================================================
# GET RECENT USER ACTIVITY
# ============================================================

def get_recent_activity(user_id, limit=5):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
        task,
        created_at

        FROM ai_history

        WHERE user_id=?

        ORDER BY id DESC

        LIMIT ?

        """,
        (
            user_id,
            limit
        )
    )


    activity = cursor.fetchall()


    conn.close()


    return activity
    # ============================================================
# GET USER AI CONTEXT
# ============================================================

def get_user_context(user_id):

    profile = get_profile(user_id)


    if profile:

        return f"""
Career Goal:
{profile[0]}

Skills:
{profile[1]}

Experience:
{profile[2]}

Education:
{profile[3]}
"""


    return "No profile information available."
