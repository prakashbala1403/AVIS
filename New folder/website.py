import streamlit as st
from PIL import Image
import json
import os
import sqlite3                             # sqlite (not use industry mostly prefer mysql)
import mysql.connector



init_db = mysql.connector.connect(
    host="shinkansen.proxy.rlwy.net",         # Railway host
    port=36048,                                # Railway port
    user="root",                               # Railway user
    password="qNctttAsIiXEpvbcaKhcHEENkEJGzNqX",  # Railway password
    
)
cursor = init_db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS babyshower_db")
init_db.close()



db = mysql.connector.connect(
    host="shinkansen.proxy.rlwy.net",         # Railway host
    port=36048,                                # Railway port
    user="root",                               # Railway user
    password="qNctttAsIiXEpvbcaKhcHEENkEJGzNqX",  # Railway password
    database="railway"                         # Railway database name
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




            
