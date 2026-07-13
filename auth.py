import sqlite3
import hashlib
from database import get_connection


# ============================
# PASSWORD HASHING
# ============================

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ============================
# CREATE USER
# ============================

def create_user(name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute(
            """
            INSERT INTO users 
            (name, email, password)
            VALUES (?, ?, ?)
            """,
            (
                name,
                email,
                hashed_password
            )
        )

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:
        conn.close()
        return False



# ============================
# LOGIN USER
# ============================

def authenticate_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    cursor.execute(
        """
        SELECT id, name, email
        FROM users
        WHERE email=? AND password=?
        """,
        (
            email,
            hashed_password
        )
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }

    return None



# ============================
# GET USER PROFILE
# ============================

def get_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, email, created_at
        FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user
