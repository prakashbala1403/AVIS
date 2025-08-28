import streamlit as st
from PIL import Image
import json
import os
import sqlite3                             # sqlite (not use industry mostly prefer mysql)
import mysql.connector

DB_HOST = "shuttle.proxy.rlwy.net"
DB_PORT = 26970
DB_USER = "root"
DB_PASS = "NSZvoNxXFEKuaCRwEIYAUKldRcoOLqYb"
DB_NAME = "railway"


init_db = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASS,
    
)
cursor = init_db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS railway")
init_db.close()



db = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
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
      invite_link=f"https://hemsinvitation.onrender.com/?name={user_name}"
      st.markdown(f"[Your Invitation Link click here>]({invite_link})")
   

cur.close()
db.close()




            
