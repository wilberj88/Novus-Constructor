import streamlit as st
from streamlit_extras.let_it_rain import rain 

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Constructor", page_icon="🏗️")

st.title('Novus Constructor 🏗️ Automated Cycle')

st.write('---')

service = st.selectbox(
        "Which service do you prefer?",
        ("Licences", "Expert Report"),
    )

if service == "Licences":
  st.header("Novus Constructor 🏗️")
  st.subheader("Say goodbye to high costs 💲 and long times ⏰")
  st.write("Charge your documents")
  
