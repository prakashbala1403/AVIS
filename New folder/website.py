import streamlit as st
from PIL import Image
import json
import os
import sqlite3                             # sqlite (not use industry mostly prefer mysql)
import mysql.connector

DB_HOST = shinkansen.proxy.rlwy.net
DB_PORT = 36048
DB_USER = root
DB_PASS = qNctttAsIiXEpvbcaKhcHEENkEJGzNqX


init_db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 3306)),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
   
)
cursor = init_db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS babyshower_db")
init_db.close()


db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 3306)),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("babyshower_db")
)
cur=db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS guest (name VARCHAR(100) PRIMARY KEY)""")

user_name=st.text_input("Enter Your Name ")
st.button("Submit")


if user_name :
    cur.execute("SELECT name from guest WHERE name =%s", (user_name,))
    result=cur.fetchone()

    if result:
      st.warning("Your name is already registered")
    else:
      cur.execute("INSERT INTO guest (name) VALUES (%s)",(user_name,))
      db.commit()
      st.success("Your name is Registered Successfully")
      invite_link=f"https://avis-1.onrender.com/?name={user_name}"
      st.markdown(f"""[Your Invitation Link click here>]({invite_link})""")
   

cur.close()
db.close()




            
