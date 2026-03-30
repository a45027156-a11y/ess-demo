import streamlit as st
from ess_engine import generate_signature, detect_anomaly
import random
import datetime

st.set_page_config(page_title="ESS 인증 데모", layout="centered")

st.title("🔐 ESS 환경 기반 인증 시스템 (Demo)")

st.write("스마트폰 환경 데이터를 기반으로 사용자 인증을 수행합니다.")

# -------------------------
# 입력 영역 (환경 데이터)
# -------------------------
st.subheader("📡 환경 데이터 입력")

location = st.text_input("위치 (예: Seoul, Home, Office)", "Seoul")
time_now = datetime.datetime.now().hour
wifi = st.selectbox("WiFi 상태", ["Home_WiFi", "Office_WiFi", "Unknown"])
motion = st.selectbox("이동 상태", ["Stationary", "Walking", "Running"])

device_noise = st.slider("센서 노이즈 레벨", 0, 100, 20)

# -------------------------
# ESS 생성
# -------------------------
if st.button("ESS 인증 실행"):

    env_data = {
        "location": location,
        "time": time_now,
        "wifi": wifi,
        "motion": motion,
        "noise": device_noise
    }

    signature = generate_signature(env_data)
    result, score = detect_anomaly(env_data)

    st.subheader("🧠 ESS 환경 서명")
    st.code(signature)

    st.subheader("📊 인증 결과")

    if result == "NORMAL":
        st.success(f"정상 인증 (유사도: {score}%)")
    else:
        st.error(f"이상 환경 감지! (유사도: {score}%)")

    st.progress(score / 100)

# -------------------------
# 로그 시뮬레이션
# -------------------------
st.subheader("📜 인증 로그 (시뮬레이션)")

if st.button("랜덤 로그 생성"):

    for i in range(5):
        fake_score = random.randint(60, 100)
        status = "NORMAL" if fake_score > 80 else "ABNORMAL"
        st.write(f"{i+1}. 상태: {status} | 유사도: {fake_score}%")
