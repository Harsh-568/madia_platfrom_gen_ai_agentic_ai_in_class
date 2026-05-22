import mysql.connector
import streamlit as st

try:
    conn_obj = mysql.connector.connect(
        host=st.secrets["host"],
        database=st.secrets["database"],
        port=int(st.secrets["port"]),   # FIXED
        user=st.secrets["user"],
        password=st.secrets["password"]
    )

    cursor_obj = conn_obj.cursor(dictionary=True)

    # USERS TABLE
    cursor_obj.execute("""
    CREATE TABLE IF NOT EXISTS users3(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        password VARCHAR(100)
    )
    """)

    # FILES TABLE
    cursor_obj.execute("""
    CREATE TABLE IF NOT EXISTS files3(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        file_name VARCHAR(255),
        file_type VARCHAR(100),
        file_url TEXT,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users3(id)
    )
    """)

    conn_obj.commit()

    st.success("Tables Created Successfully")

except mysql.connector.Error as err:
    st.error(f"MySQL Error: {err}")

except Exception as e:
    st.error(f"Error: {e}")

finally:
    if 'cursor_obj' in locals():
        cursor_obj.close()

    if 'conn_obj' in locals() and conn_obj.is_connected():
        conn_obj.close()