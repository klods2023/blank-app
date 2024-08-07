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