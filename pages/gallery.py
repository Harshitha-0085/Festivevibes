import streamlit as st

def show_gallery():

    st.title("📸 Telugu Festival Gallery")

    festivals = [
        {
            "name":"Bathukamma",
            "image":"https://images.unsplash.com/photo-1513151233558-d860c5398176?q=80&w=1200&auto=format&fit=crop",
            "description":"Beautiful flower festival of Telangana"
        },

        {
            "name":"Sankranti",
            "image":"https://images.unsplash.com/photo-1545239351-1141bd82e8a6?q=80&w=1200&auto=format&fit=crop",
            "description":"Harvest festival celebrated with kites and rangoli"
        },

        {
            "name":"Bonalu",
            "image":"https://images.unsplash.com/photo-1529156069898-49953e39b3ac?q=80&w=1200&auto=format&fit=crop",
            "description":"Traditional Telangana festival dedicated to Goddess Mahakali"
        },

        {
            "name":"Ugadi",
            "image":"https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=1200&auto=format&fit=crop",
            "description":"Telugu New Year celebration"
        }
    ]

    cols = st.columns(2)

    for i,festival in enumerate(festivals):

        with cols[i % 2]:

            st.image(
                festival["image"],
                use_container_width=True
            )

            st.markdown(f"""

            <div class='festival-card'>

            <h3>{festival['name']}</h3>

            <p>{festival['description']}</p>

            </div>

            """, unsafe_allow_html=True)
