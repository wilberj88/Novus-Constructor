import streamlit as st
from streamlit_extras.let_it_rain import rain 

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Constructor", page_icon="🏗️")

st.title('Novus Constructor 🏗️')
st.header('⚙️ · 🤖 Automated Cycle · 🦾 · 🛠️')
st.subheader("Say goodbye to high costs 💲 and long times ⏰")
st.write('---')

service = st.selectbox(
        "Which service do you prefer?",
        ("Licences", "Expert Report"),index=None,
    placeholder="Select an automated service, you just need your documents to charge..."
    )

if service == "Licences":
  st.header("Novus Constructor 🏗️")
  st.write("Charge your documents")
  
