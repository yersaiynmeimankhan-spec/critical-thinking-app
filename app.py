import streamlit as st

st.title("🧠 Critical Thinking Simulator")

# 20 сұрақтан тұратын база
questions = [
    {"q": "Қымбат фермерлік өнімдерді алатын адамдар ұзақ өмір сүреді. Демек, фермерлік тамақ өмірді ұзартады. Қателік неде?", "a": "Корреляция – себеп емес (correlation does not imply causation)"},
    {"q": "Барлық аққулар ақ. Демек, қара аққу жоқ. Бұл қандай логикалық қателік?", "a": "Асығыс қорытынды"},
    {"q": "Егер сен маған қосылмасаң, онда сен маған қарсысың. Бұл қандай қателік?", "a": "Жалған дилемма"},
    # ... осылай 20 сұраққа дейін қоса бересің
]

# Сұрақтарды толтырып болған соң, қосымша сұрақтарды мына форматта қосасың:
# {"q": "Сұрағың", "a": "Жауабың"},

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

current_q = questions[st.session_state.q_index]

st.write(f"### {st.session_state.q_index + 1}-сұрақ: {current_q['q']}")
user_ans = st.text_input("Жауабың:", key="ans")

if st.button("Тексеру"):
    if user_ans.strip().lower() == current_q['a'].lower():
        st.success("Дұрыс! +10 XP")
        st.session_state.score += 10
        st.session_state.q_index = (st.session_state.q_index + 1) % len(questions)
        st.rerun()
    else:
        st.error("Қате, қайталап көр!")

st.write(f"### Сенің ұпайың: {st.session_state.score} XP")