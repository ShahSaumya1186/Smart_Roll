import streamlit as st
from src.Components.header import header_home
from src.Ui.base_layout import style_base_layout

def home_screen():
    st.header("Home screen")
    header_home()
    style_base_layout()
    col1, col2 = st.columns(2)
    with col1:
    #    separating two columns of techer and student column
       if st.button("Teache Portal"):
           st.session_state['login_type'] = 'teacher'
           st.rerun()
    with col2:
        if st.button("Student Portal"):
            st.session_state['login_type'] = 'student'
            st.rerun()
home_screen()