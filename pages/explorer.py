import streamlit as st
from utils.fetch_data import fetch_festival_data

def show_festival_explorer():

    st.title("🎊 Festival Explorer")

    festival = st.text_input(
        "Search Telugu Festival"
    )

    if festival:

        with st.spinner("Searching festival..."):

            data = fetch_festival_data(festival)

        if data:

            st.markdown(f"""

            <div class='festival-card'>

            <h1>{data["title"]}</h1>

            <p>{data["summary"]}</p>

            <a href="{data["url"]}" target="_blank">
            Read More
            </a>

            </div>

            """, unsafe_allow_html=True)

        else:

            st.error(
                "Festival not found"
            )
