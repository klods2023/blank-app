import streamlit as st
from streamlit_login_auth_ui.widgets import Login

login_obj = Login(auth_token="courier_auth_token", 
                  company_name="Shims",
                  width=200, height=250, 
                  logout_button_name='Logout', hide_menu_bool=False, 
                  hide_footer_bool=False, 
                  lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = login_obj.build_login_ui()

if LOGGED_IN == True:
    st.markdown("Your Streamlit Application Begins here!")