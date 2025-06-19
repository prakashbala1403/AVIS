import streamlit as st
from PIL import Image
import json
import os


st.markdown("""
<div style="background-color:#f3e5f5;padding:20px;border-radius:12px;text-align:center;">
    <h1 style="color:#6a1b9a;">🌼 Seemandham 🌼</h1>
    <p style="font-size:18px; color:#4a148c;">A joyful celebration of tradition, love, and new beginnings</p>
</div>
""", unsafe_allow_html=True)



st.markdown("""
<h1 style="color:green;">Join Us For A Baby Shower</h1>""", unsafe_allow_html=True)




img = Image.open(r"C:\Users\user\Downloads\seemandham.jpg")
img_re=img.resize((400,600))

img1 = Image.open(r"C:\Users\user\Downloads\foots.jpg")
img_re1=img1.resize((100,200))

col1, col2, col3 = st.columns([1, 2, 1]) 

with col1:
    st.markdown("""<h1 style="color:purple;font-size:20px;">In Honor of MOM-TO-BE</h1>""", unsafe_allow_html=True)  
    st.markdown("""<h1 style="color:violet;font-size:20px;">HEMA PRAKASH</h1>""", unsafe_allow_html=True)
    st.image(img_re1, caption="boy | girl")
with col2:
    st.image(img_re, caption="Seemandham Event")
    st.markdown("""<h2 style="color:brown;font-size:20px;text-align:center;">Aug 29-Friday-9:00AM</h2>""", unsafe_allow_html=True)
    




vote_file = "votes.json"

# Initialize file if it doesn't exist
if not os.path.exists(vote_file):
    with open(vote_file, "w") as f:
        json.dump({"Boy": 0, "Girl": 0}, f)

# Load current vote counts
with open(vote_file, "r") as f:
    votes = json.load(f)      # Just read boy 0 and girl 0

# UI - voting buttons
st.title("🌟 Vote Now!")
col1, col2 = st.columns(2)

with col1:
    if st.button("👦 Vote for Boy"):
        votes["Boy"] += 1

with col2:
    if st.button("👧 Vote for Girl"):
        votes["Girl"] += 1

# Save updated counts
with open(vote_file, "w") as f:
    json.dump(votes, f)

# Display current results
st.markdown("### 📊 Current Vote Counts:")
st.write(f"👦 Boy: {votes['Boy']} votes")
st.write(f"👧 Girl: {votes['Girl']} votes")