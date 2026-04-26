import streamlit as st
import pandas as pd
import time

# 1. Бет параметрлері
st.set_page_config(page_title="Advanced Critical Thinking", page_icon="🧠", layout="centered")

# 2. CSS стильдері
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: white; }
    .glass-card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; margin-bottom: 20px; }
    div.stButton > button { background-color: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid rgba(255, 255, 255, 0.3) !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# 3. Негізгі мәтін
st.title("🧠 Critical Thinking Simulator")
st.write("Сәлем! Бұл - сенің алғашқы веб-жобаң. Жұмыс істеп тұр!")

if 'score' not in st.session_state:
    st.session_state.score = 0

if st.button("Ұпай қосу"):
    st.session_state.score += 10
    st.rerun()

st.write(f"### Сенің ұпайың: {st.session_state.score} XP")