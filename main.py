import streamlit as st
from streamlit_extras.let_it_rain import rain 

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
        st.subheader('Land 🗺️')
        st.text("""
        1. Asset Certificate
        2. Taxes Certificate
        3. Contract of Sale
        """)
        uploaded_files = st.file_uploader(
            "Charge the 3 documents here:", accept_multiple_files=True
        )
        
        if uploaded_files:
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)

        st.subheader('Constructor 👷')
        st.text("""
        1. Professional Certificate
        """)

        st.subheader('Topography ⛰️')
        st.text("""
        1. Topographic Survey
        """)

        st.subheader('Structural 🏛️')
        st.text("""
        1. Structural Analysis
        """)

        st.subheader('Architecture 🏛️')
        st.text("""
        1. Architecture Design
        """)

        st.subheader('Hydrosanitary ware 💦')
        st.text("""
        1. Hydrosanitary Report
        """)
            
        st.subheader('Electric ⚡')
        st.text("""
        1. Electric Report
        """)

        st.subheader('No Structural 🧱')
        st.text("""
        1. No Structural Report
        """)
            
        submitted = st.form_submit_button("Submit")
