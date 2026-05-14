import streamlit as st

def load_css():

    st.markdown("""
    <style>

    [data-testid="stAppViewContainer"]{
        background:linear-gradient(to bottom,#0f172a,#1e1b4b);
        color:white;
    }

    .main-header{
        background:linear-gradient(135deg,#7c3aed,#ec4899);
        padding:5rem;
        border-radius:30px;
        text-align:center;
        margin-bottom:3rem;
    }

    .festival-card{
        background:rgba(255,255,255,0.08);
        backdrop-filter:blur(10px);
        padding:25px;
        border-radius:20px;
        margin-bottom:20px;
    }

    </style>
    """, unsafe_allow_html=True)
