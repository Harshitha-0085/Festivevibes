import streamlit as st
import random
from app import get_festival_data

def show_homepage():

    festivals = get_festival_data()

    st.markdown("""

    <div class='main-header'>

    <h1>🎉 FestiveVibe</h1>

    <h3>
    Celebrating Telugu Festivals & Heritage
    </h3>

    </div>

    """, unsafe_allow_html=True)

    spotlight = random.choice(list(festivals.keys()))

    st.info(f"🌟 Festival Spotlight: {spotlight}")

    cols = st.columns(2)

    for i,(festival,data) in enumerate(festivals.items()):

        with cols[i%2]:

            st.markdown(f'''
            <div class='festival-card'>

            <h3>{festival}</h3>

            <p>{data["description"]}</p>

            <p>📅 {data["date"]}</p>

            </div>
            ''', unsafe_allow_html=True)
