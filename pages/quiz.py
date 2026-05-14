import streamlit as st

def show_quiz():

    st.title("🧠 Telugu Festival Quiz")

    score = 0

    q1 = st.radio(
        "Which festival is known as the floral festival of Telangana?",
        ["Bonalu","Bathukamma","Ugadi","Dasara"]
    )

    q2 = st.radio(
        "Which festival marks Telugu New Year?",
        ["Sankranti","Ugadi","Bonalu","Holi"]
    )

    if st.button("Submit Quiz"):

        if q1 == "Bathukamma":
            score += 1

        if q2 == "Ugadi":
            score += 1

        st.success(f"🎉 Your Score: {score}/2")
      
