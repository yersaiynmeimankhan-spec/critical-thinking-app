import streamlit as st

st.title("🧠 Critical Thinking Simulator")
st.write("Сәлем! Бұл - сенің алғашқы веб-жобаң.")

# Сессиялық күйді инициализациялау (егер жоқ болса)
if 'score' not in st.session_state:
    st.session_state.score = 0

# Батырманы басу логикасы
if st.button("Ұпай қосу"):
    st.session_state.score += 10
    # Скриптті қайта жүктеудің қажеті жоқ, 
    # Streamlit батырма басылғанда бетті автоматты түрде жаңартады.

# Ұпайды көрсету
st.write(f"### Сенің ұпайың: {st.session_state.score} XP")