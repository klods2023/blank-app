import streamlit as st

# Создаем форму регистрации
name = st.text_input('Введите ваше имя', '')
email = st.text_input('Введите ваш email', '')
password = st.text_input('Введите пароль', type='password')
confirm_password = st.text_input('Подтвердите пароль', type='password')

if st.button('Зарегистрироваться'):
    if password == confirm_password:
        st.write(f'Регистрация прошла успешно! Добро пожаловать, {name}!')
    else:
        st.write('Пароли не совпадают. Попробуйте еще раз.')


import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "courier_auth_token", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.markown("Your Streamlit Application Begins here!")