import streamlit as st

from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.footer import footer_dashboard
from src.database.db import check_teachers_exists,create_teachers,teacher_login

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type=='Register':
        teacher_screen_register()

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data

    st.header(f"""Welcome, {teacher_data['name']} """)


def login_teacher(username,password):
    if not username or not password:
        return False

    teacher=teacher_login(username,password)

    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True

    return False


     


def register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False,"All feilds are required"
    if check_teachers_exists(teacher_username):
        return False,"Username already taken"
    if teacher_pass!=teacher_pass_confirm:
        return False,"Password doesn't match"

    try:
        create_teachers(teacher_username,teacher_pass,teacher_name)
        return True,"Sucessfully Created! Login Now"
    except Exception as e:
        return False,e

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
        if st.button("login",type="secondary",shortcut="control + enter",icon=":material/passkey:",width="stretch"):
            if login_teacher(teacher_username,teacher_passward):
                st.toast("Welcome back!")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Username and Password Combo")
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
        if st.button("Register Now",type="secondary",shortcut="control + enter",icon=":material/passkey:",width="stretch"):
            success,message=register_teacher(teacher_username,teacher_name,teacher_passward,teacher_passward_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type='login'
                st.rerun()
            else:
                st.error(message)
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
