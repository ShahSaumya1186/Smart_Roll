import streamlit as st
from src.Components.header import header_home
from src.Components.footer import footer_home
from src.Ui.base_layout import style_base_layout,style_background_home

def home_screen():
    # st.header("Home screen")
    header_home()
    style_base_layout()
    style_background_home()
    col1, col2 = st.columns(2,gap="large")
    with col1:
    #    separating two columns of techer and student column
        st.header("I'm Teacher")
        st.image("C:/Users/SAUMYA/Downloads/snap-teacher.png", width=220)
        if st.button("Teacher Portal",key="primary",icon=':material/arrow_outward:'):
           st.session_state['login_type'] = 'teacher'
           st.rerun()
    with col2:
        st.header("I'm Student")
        st.image("C:/Users/SAUMYA/Downloads/snap-student.png", width=220)
        if st.button("Student Portal",key="secondary",icon=':material/arrow_outward:'):
            st.session_state['login_type'] = 'student'
            st.rerun()
    footer_home()