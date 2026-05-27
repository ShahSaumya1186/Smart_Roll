import streamlit as st
from src.Screens.home_screen import home_screen
from src.Screens.student_screen import student_screen
from src.Screens.teacher_screen import teacher_screen
def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()
main()