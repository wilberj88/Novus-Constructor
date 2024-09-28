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
    with st.form("registry"):
        st.subheader('Registry & Activation Process 📝⚙️')
        st.write("""
        **Land Documents**
        1. Asset Certificate
        2. Taxes Certificate
        3. Contract of Sale

        **Professionals Documents**
        1. Constructor Company Certificate 🏗️
        2. Topographic Company ⛰️
        3. Structural Company 🏛️
        4. Architecture Company 🏛️
        5. Hydrosanitary Company 💦
        6. Electric Company ⚡
        7. No Structural Company 🧱

        **Project Documents**
        1. Topographic Survey ⛰️
        2. Structural Analysis 🏛️
        3. Architecture Design 🏛️
        5. Hydrosanitary Report 💦
        6. Electric Report ⚡
        7. No Structural Report 🧱
        
        """)
        uploaded_files1 = st.file_uploader(
            "Charge the 17 documents here:", accept_multiple_files=True
        )
        
        if uploaded_files1:
            for uploaded_file in uploaded_files1:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
        
    submitted = st.form_submit_button("Activate License Review RIGTH NOW")
    if submitted:
        st.write("""
        **Your project is now in review** 🤖⏰🧠
        In just 3 days you will recive our Final Report with % of Compliance & Recommendations to achive 100% for License Aprobation
        """)

