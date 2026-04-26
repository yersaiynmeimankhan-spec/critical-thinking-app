import streamlit as st

st.title("🧠 Critical Thinking Simulator")

# Сұрақтар мен нұсқалар базасы
questions = [
    {
        "q": "Қымбат фермерлік өнімдерді алатын адамдар ұзақ өмір сүреді. Демек, фермерлік тамақ өмірді ұзартады. Қателік неде?",
        "options": [
            "Асығыс қорытынды жасау", 
            "Корреляция – себеп емес (correlation does not imply causation)", 
            "Жалған дилемма", 
            "Адамның жеке басына тиісу"
        ],
        "answer": "Корреляция – себеп емес (correlation does not imply causation)"
    },
    {
        "q": "Барлық аққулар ақ. Демек, қара аққу мүлдем жоқ. Бұл қандай логикалық қателік?",
        "options": [
            "Асығыс қорытынды", 
            "Дәлелдеу жүгін аудару", 
            "Авторитетке жүгіну", 
            "Строумен (Қаратұлып) аргументі"
        ],
        "answer": "Асығыс қорытынды"
    }
    # Осы жерге қалған 18 сұрақты үтірмен бөліп қоса бересің
]

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

# --- ПЬЕДЕСТАЛ (Деңгейлер) ---
score = st.session_state.score
if score < 20:
    level = "Жаңадан бастаушы 🥉"
elif score < 40:
    level = "Танымпаз 🥈"
elif score < 60:
    level = "Логика шебері 🥇"
else:
    level = "Критикалық ойлау данышпаны 👑"

st.write(f"### 🏆 Сенің дәрежең: {level}")
st.write(f"**Ұпайың:** {score} XP")
st.progress(min(score / 100, 1.0)) # Прогресс жолағы (100 ұпайға дейін)
st.markdown("---")

# --- СҰРАҚ ЖӘНЕ ЖАУАПТАР ---
current_q = questions[st.session_state.q_index]

st.write(f"### Сұрақ {st.session_state.q_index + 1}:")
st.info(current_q['q'])

# Жауап нұсқаларын радио-батырмамен шығару
choice = st.radio("Дұрыс нұсқаны таңда:", current_q['options'])

if st.button("Тексеру"):
    if choice == current_q['answer']:
        st.success("Дәл таптың! +10 XP 🔥")
        st.session_state.score += 10
        # Келесі сұраққа өту
        st.session_state.q_index = (st.session_state.q_index + 1) % len(questions)
        st.rerun()
    else:
        st.error("Қате! Тағы бір рет ойланып көрші. 🧐")