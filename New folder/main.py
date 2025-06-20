import pandas as pd
import os
import streamlit as st
import json
from PIL import Image 









col1,col2,col3=st.columns(3)


with col2:
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Courgette&display=swap" rel="stylesheet">
    <style>
    .invitation {
        font-family: 'Courgette', cursive;
        color: #DA70D6;
        font-size: 28px;
        text-align: center;
    }
    </style>
    <div class='invitation'>
        You’re Invited!<br>
        
    </div>
""", unsafe_allow_html=True)
st.markdown("""
<div style="background-color:#f3e5f5;padding:20px;border-radius:12px;text-align:center;">
    <h1 style="color:#6a1b9a;font-family: 'Courgette', cursive;font-size:18px">🌼 Baby Shower 🌼</h1>
    <p style="font-size:18px; color:#4a148c;font-family: 'Brush Script MT',cursive;">A joyful celebration of tradition, love, and new beginnings</p>
</div>
""", unsafe_allow_html=True)








img = Image.open("seemandham.jpg")
img_re=img.resize((400,600))

img1 = Image.open("foots.jpg")
img_re1=img1.resize((400,100))

col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
          st.markdown("""
<h2 style="color:green;font-family: 'Courgette', cursive;text-align:center;">Join Us For A Baby Shower</h1>""", unsafe_allow_html=True)
          st.markdown("""<h1 style="color:purple;font-size:20px;font-family:'Courgette', cursive;text-align:center;">In Honor of MOM-TO-BE</h1>""", unsafe_allow_html=True)  
          st.markdown("""<h1 style="color:violet;font-size:30px;font-family:'Courgette', cursive;text-align:center;">HEMA PRAKASH</h1>""", unsafe_allow_html=True)
          st.image(img_re1, caption="boy | girl")

          st.image(img_re, caption="Seemandham Event")
          st.image(img_re1, caption="boy | girl")
          st.markdown("""<h2 style="color:brown;font-size:20px;text-align:center;font-family: 'Courgette', cursive;">Friday, Aug 29, 2025, 9:00 AM</h2>""", unsafe_allow_html=True)
          st.markdown("""<h2 style="color:brown;font-size:20px;text-align:center;font-family: 'Courgette', cursive;">Venue : RKS MAHAL, Avadi</h2>""", unsafe_allow_html=True)






name_file="final.json"

if os.path.exists(name_file):
       with open(name_file,"r") as f:
              votes=json.load(f)
else:
       votes={"Boy":[],
              "Girl":[]
              }

user_name=st.text_input("Enter_Name")
col1, col2 = st.columns(2)
with col1:
 if st.button("👦 Vote for Boy"):
       if user_name not in votes["Boy"] and user_name not in votes["Girl"]:
              votes["Boy"].append(user_name)

              with open(name_file, "w") as f:
                    json.dump(votes, f)
                    st.success(f"✅ Thanks {user_name}, your vote for Boy has been saved!")
                    st.markdown("""<h2 style="color:brown;font-size:20px;text-align:center;font-family: 'Courgette', cursive;">We value your participation — your vote means a lot! 🎉</h2>""", unsafe_allow_html=True)

       else:
                st.warning("⚠️ You have already voted.")
 else:
            st.warning("⚠️ Please enter your name before voting.")


with col2:
 if st.button("👧 Vote for Girl"):
       if user_name not in votes["Girl"] and user_name not in votes["Boy"]:
              votes["Girl"].append(user_name)

              with open(name_file, "w") as f:
                    json.dump(votes, f)
                    st.success(f"✅ Thanks {user_name}, your vote for Girl has been saved!")
                    st.markdown("""<h2 style="color:brown;font-size:20px;text-align:center;font-family: 'Courgette', cursive;">We value your participation — your vote means a lot! 🎉</h2>""", unsafe_allow_html=True)
       else:
                st.warning("⚠️ You have already voted.")
 else:
            st.warning("⚠️ Please enter your name before voting.")
