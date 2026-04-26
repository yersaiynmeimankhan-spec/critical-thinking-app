import streamlit as st

st.title("🧠 Critical Thinking Simulator")

# Сұрақтар қоры
questions = [
    {"question": "Магнит өрісіндегі тогы бар өткізгішке әрекет ететін күш қалай аталады?", "answer": "Ампер күші"},
    {"question": "Жарықтың екі орта шекарасында шағылуы қалай аталады?", "answer": "Толық ішкі шағылу"},
    {"question": "Атом ядросы неден тұрады?", "answer": "Протон мен нейтрон"}
]

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

q = questions[st.session_state.q_index]

st.write(f"### Сұрақ: {q['question']}")
answer = st.text_input("Жауабыңды жаз:")

if st.button("Жауапты тексеру"):
    if answer.strip().lower() == q['answer'].lower():
        st.success("Дұрыс! +10 XP")
        st.session_state.score += 10
        st.session_state.q_index = (st.session_state.q_index + 1) % len(questions)
    else:
        st.error("Қате, қайталап көр!")

st.write(f"### Сенің ұпайың: {st.session_state.score} XP")