import streamlit as st
from streamlit_option_menu import option_menu

from utils.styles import load_css
from pages.homepage import show_homepage
from pages.explorer import show_festival_explorer
from pages.quiz import show_quiz
from pages.gallery import show_gallery

load_css()

selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "Explorer",
        "Quiz",
        "Gallery"
    ],
    icons=[
        "house-fill",
        "stars",
        "controller",
        "images"
    ],
    orientation="horizontal"
)

if selected == "Home":
    show_homepage()

elif selected == "Explorer":
    show_festival_explorer()

elif selected == "Quiz":
    show_quiz()

elif selected == "Gallery":
    show_gallery()
