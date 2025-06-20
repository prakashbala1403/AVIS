import streamlit as st
from PIL import Image
import json
import os

name_file = "name.json"


if os.path.exists(name_file):
      with open(name_file,"r") as f:
            names=json.load(f)
else:
      names=[]




user_name=st.text_input("Please enter your name") #------------ First

if st.button("Submit button"):
        if user_name not in names:
            names.append(user_name)
            with open(name_file,"w") as f:
                    json.dump(names,f)   

            st.success("✅ Your name is registered!")
            st.markdown("[💌 You are invited! Please click here >](https://https://seemandha.streamlit.app/)")
            
        else:
            st.warning("⚠️ This name has already been registered.")
else:
            st.write("please enter you name before submitting")


            
