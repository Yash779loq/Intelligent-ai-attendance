import streamlit as st

from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type=='Register':
        teacher_screen_register()


    

def teacher_screen_login():
    # top header
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("go back to home",type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state["login_type"]=None
            st.rerun()

    st.header("login using passward",text_alignment='center')
    st.space()
    st.space()

    # login info
    teacher_username=st.text_input("Enter Username",placeholder="enter")

    teacher_passward=st.text_input("Enter Passward",type="password",placeholder="Enter Passward")

    st.divider()

    #login register button
    btnc1,btnc2=st.columns(2,vertical_alignment='center')
    with btnc1:
        st.button("login",type="secondary",shortcut="control + enter",icon=":material/passkey:",width="stretch")
    with btnc2:
        if st.button("Register Instead",type="primary",icon=":material/passkey:",width="stretch"):
            st.session_state.teacher_login_type='Register'
            st.rerun()


    footer_dashboard()


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("go back to home",type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.session_state.teacher_login_type='login'
            st.rerun()

    st.header("Register account",text_alignment='center')
    st.space()
    st.space()

    # login info
    teacher_username=st.text_input("Enter Username",placeholder="enter")

    teacher_name=st.text_input("Enter name",placeholder="enter")
    
    teacher_passward=st.text_input("Enter Passward",type="password",placeholder="Enter Passward")

    teacher_passward_confirm=st.text_input("Confirm Passward",type="password",placeholder="Confirm Passward")

    st.divider()

    btnc1,btnc2=st.columns(2,vertical_alignment='center')
    with btnc1:
        st.button("Register Now",type="secondary",shortcut="control + enter",icon=":material/passkey:",width="stretch")
    with btnc2:
        if st.button("Login Instead",type="primary",icon=":material/passkey:",width="stretch"):
            st.session_state.teacher_login_type='login'
            st.rerun()

    footer_dashboard()

# def teacher_dashboard():
#     teacher_data = st.session_state.teacher_data
#     c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
#     with c1:
#         header_dashboard()
#     with c2:
#         st.subheader(f"""Welcome, {teacher_data['name']} """)
#         if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
#             st.session_state['is_logged_in'] = False
#             del st.session_state.teacher_data 
#             st.rerun()
