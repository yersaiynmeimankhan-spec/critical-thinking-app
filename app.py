import streamlit as st

# 1. Бет параметрлері
st.set_page_config(page_title="Critical Thinking", page_icon="🧠", layout="centered")

# 2. CSS стильдері (Бұл код кнопкалар мен мәтінді көрінетін қылады)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: white;
    }
    /* Кнопкалардың дизайны */
    div.stButton > button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
    }
    div.stButton > button:hover {
        background-color: rgba(0, 242, 254, 0.2) !important;
        border-color: #00f2fe !important;
    }
    /* Мәтін түсі */
    h1, h2, h3, p { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. Тесттік бөлім
st.title("🧠 Логикалық ойлауды дамыту")
st.write("Сұраққа жауап беріп, өзіңді сынап көр:")

# Тесттік сұрақ
st.subheader("Сұрақ 1: Логикалық тұзақтар")
st.write("Блогердің пікірінде қандай қателік бар?")

# Кнопкалар (олар енді көрінетін болады)
if st.button("A. Тірі қалғандар қателігі"):
    st.error("Қате!")
if st.button("B. Табиғатқа жүгіну"):
    st.error("Қате!")
if st.button("C. Корреляция мен себеп-салдар"):
    st.success("Дұрыс! Ұпай қосылды!")
    if 'score' not in st.session_state: st.session_state.score = 0
    st.session_state.score += 10
    st.rerun()
if st.button("D. Жалған дилемма"):
    st.error("Қате!")

if 'score' in st.session_state:
    st.write(f"### Сенің ұпайың: {st.session_state.score}")