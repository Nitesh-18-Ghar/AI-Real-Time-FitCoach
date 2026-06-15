import streamlit as st
from services.ui.basic_layout import style_login_page, style_base_layout
from services.persistance.exercise_repository import get_or_create_user
    

def render_login_wall():

    style_login_page()
    style_base_layout()

    if st.session_state.get("user_id") is not None:
        return True
    
    st.markdown("""
        <div style="text-align:center;">
            <img src="https://i.ibb.co/G3d8BYk3/Fit-Coach-Logo.png" width="120" style="margin-top: 20px">
        </div>
        """, unsafe_allow_html=True)
    
    st.title("🏋️‍♂️ AI Real-Time GYM Trainer")
    st.markdown("### Welcome! Please Enter Your Username To Start")

    col1 = st.columns(1)[0]
    with col1:
        username = st.text_input("Username", placeholder="Unique Username e.g niteshkghar")
        if st.button("Start Session", type="primary", width="stretch"):
            if username:

                user = get_or_create_user(username)

                st.session_state["user_id"] = user["id"]
                st.session_state["username"] = user["username"]
                st.session_state['login_type'] = 'user'
                st.rerun()
            else:
                st.warning("Please Enter Your Username!")
            