import mysql.connector
import streamlit  as st

conn_obj=mysql.connector.connect(
    host = st.secrets["host"],
    database=st.secrets["database"],
    port=st.secrets["port"],
    user=st.secrets["user"],
    password=st.secrets["password"]
)

cursor_obj=conn_obj.cursor(dictionary=True)




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
    FOREIGN KEY(user_id) REFERENCES users(id)
    FOREIGN KEY(user_id) REFERENCES users3(id)
)
""")

conn.commit()
conn_obj.commit()

print("Tables Created Successfully")