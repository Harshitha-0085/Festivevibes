import streamlit as st
from utils.data import get_festival_data

def show_festival_explorer():

    festivals = get_festival_data()

    st.title("🎊 Festival Explorer")

    for festival,data in festivals.items():

        st.markdown(f"""

        <div class='festival-card'>

        <h3>{festival}</h3>

        <p>{data["description"]}</p>

        <p>📅 {data["date"]}</p>

        </div>

        """, unsafe_allow_html=True)
