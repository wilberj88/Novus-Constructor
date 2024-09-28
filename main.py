import streamlit as st
import pandas as pd
from io import StringIO

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Constructor", page_icon="🏗️")

st.title('Novus Constructor 🏗️')
st.header(' · ⚙️ · 🤖 Automated Cycle · 🦾 · 🧠')
st.subheader("Say goodbye to high costs 💰 and long times ⏰")
st.write('---')

service = st.selectbox(
        "Which service do you prefer?",
        ("Licences", "Expert Report"),
        index=None,
        placeholder="Select an automated service, you just need your documents to charge..."
    )

if service == "Licences":
    st.header("Automated Licences Review 🔎")
    st.text("Prepare and charge your documents")
    with st.form("licence_review"):
        st.subheader('Registry 🗺️')
        st.text("""
        **Land Documents**
        1. Asset Certificate
        2. Taxes Certificate
        3. Contract of Sale
        ***Professionals Documments***
        1. Constructor Certificate 🏗️
        2. Topographic Survey ⛰️
        3. Structural Analysis 🏛️
        4. Architecture Design 🏛️
        5. Hydrosanitary Report 💦
        6. Electric Report ⚡
        7. No Structural Report 🧱
        """)
        uploaded_files1 = st.file_uploader(
            "Charge the 10 documents here:", accept_multiple_files=True
        )
        
        if uploaded_files1:
            for uploaded_file in uploaded_files1:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
        
        def registry_message(): 
            st.write('Your Registry is Done')
            
        submitted = st.form_submit_button("Submit Registry", on_click=registry_message)
