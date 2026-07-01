import streamlit as st
import dlib
from src.Screens.home_screen import home_screen
from src.Screens.student_screen import student_screen
from src.Screens.teacher_screen import teacher_screen


def main():
    st.set_page_config(
        page_title="SmartRoll-Making Attendance Faster Using AI",
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None
    match st.session_state["login_type"]:
        case 'teacher': 
            teacher_screen()
        case 'student':
            student_screen()
        case _:
            home_screen()


if __name__ == "__main__":
    main()
