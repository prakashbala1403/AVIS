import pandas as pd
import os
import streamlit as st
import json
from PIL import Image
import mysql.connector 


DB_HOST = "shinkansen.proxy.rlwy.net"
DB_PORT = 36048
DB_USER = "root"
DB_PASS = "qNctttAsIiXEpvbcaKhcHEENkEJGzNqX"
DB_NAME = "railway"





query=st.query_params
user_name=query.get("name","")           #-----> First need to write query.get()[0]

db = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
cur = db.cursor()

# --- Create votes table if not exists ---
cur.execute("""
CREATE TABLE IF NOT EXISTS votes (
    name VARCHAR(100) PRIMARY KEY,
    vote VARCHAR(10)
)
""")



col1,col2,col3=st.columns(3)


with col2:
    st.markdown(f"""<h1 style="font-family: 'Courgette', cursive;color: #ff69b4;font-size: 28px;
        text-align: center;">Hey {user_name} You’re Invited!</h1>""", unsafe_allow_html=True)
    
st.markdown("""
<div style="background-color:#add8e6;padding:20px;border-radius:12px;text-align:center;">
    <h1 style="color:blue;font-family: 'Courgette', cursive;font-size:34px">🌼 Baby Shower 🌼</h1>
    <p style="font-size:28px; color:blue;font-family: 'Brush Script MT',cursive;">A joyful celebration of tradition, love, and new beginnings</p>
</div>
""", unsafe_allow_html=True)








img = Image.open(r"New folder/seemandham.jpg")
img_re=img.resize((400,600))

img1 = Image.open(r"New folder/foots.jpg")
img_re1=img1.resize((400,100))

img2 = Image.open(r"New folder/baby.jpeg")
img_re2=img2.resize((400,300))

img3 = Image.open(r"New folder/Boy.jpeg")
img_re3=img3.resize((400,300))

img4 = Image.open(r"New folder/Girl.jpeg")
img_re4=img4.resize((400,300))



col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
          st.markdown("""
<h2 style="color:#ff69b4;font-family: 'Courgette', cursive;text-align:center;">Join Us For A Baby Shower</h1>""", unsafe_allow_html=True)
          st.markdown("""<h1 style="color:blue;font-size:20px;font-family: 'Courgette', cursive;text-align:center;">In Honor of mom-to-be</h1>""", unsafe_allow_html=True)  
          st.markdown("""<h1 style="color:#ff69b4;font-size:30px;font-family: "Lobster", cursive;text-align:center;">🎀  Hema Prakash  🎀</h1>""", unsafe_allow_html=True)
          st.image(img_re1)
          st.image(img_re)
          
          st.markdown("""<h2 style="color:blue;font-size:20px;text-align:center;font-family: 'Courgette', cursive;">Friday, Aug 29, 2025, 9:00 AM</h2>""", unsafe_allow_html=True)
          st.markdown("""<h2 style="color:#ff69b4;font-size:20px;text-align:center;font-family: 'Courgette', cursive;">Venue : RKS mahal, Avadi</h2>""", unsafe_allow_html=True)


st.markdown("""<h2 style="color:#ff69b4;font-size:20px;text-align:center;font-family: 'Courgette', cursive;">💙 Blue or Pink, what do you think? 💗</h2>""", unsafe_allow_html=True)

cur.execute("SELECT vote FROM votes WHERE name = %s", (user_name,))
existing_vote = cur.fetchone()

if existing_vote:
    st.info(f"✅ You already voted for: **{existing_vote[0]}**")
else:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👦 Vote for Boy"):
            cur.execute("INSERT INTO votes (name, vote) VALUES (%s, %s)", (user_name, "Boy"))
            db.commit()
            st.image(img_re3)
            st.success("✅ Your vote for Boy has been saved!")
            st.markdown("""<h2 style="color:blue;font-size:20px;text-align:center;font-family: 'Courgette', cursive;"> Voting has ended — results will be announced soon!</h2>""", unsafe_allow_html=True)

    with col2:
        if st.button("👧 Vote for Girl"):
            cur.execute("INSERT INTO votes (name, vote) VALUES (%s, %s)", (user_name, "Girl"))
            db.commit()
            st.image(img_re4)
            st.success("✅ Your vote for Girl has been saved!")
            st.markdown("""<h2 style="color:#ff69b4;font-size:20px;text-align:center;font-family: 'Courgette', cursive;"> Voting has ended — results will be announced soon!</h2>""", unsafe_allow_html=True)
cur.close()
db.close()
