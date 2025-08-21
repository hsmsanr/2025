import streamlit as st
import random

# 🎨 앱 꾸미기
st.set_page_config(page_title="🌟 MBTI 진로 추천 🌟", page_icon="🎯", layout="centered")

# 💡 MBTI 별 직업 추천 데이터
career_dict = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 분석가", "🔬 연구원"],
    "ENTP": ["🚀 기업가", "🎨 마케팅 기획자", "💡 스타트업 창업자"],
    "ESFP": ["🎉 이벤트 플래너", "🎤 연예인 매니저", "📢 홍보 담당자"],
    "INFJ": ["🤝 상담가", "✍️ 작가", "📚 교사"],
    "ISTJ": ["📂 회계사", "⚖️ 법률가", "🏢 공무원"],
    "ENFP": ["🌈 크리에이터", "🎬 영화 제작자", "🌍 여행 기획자"],
    "ISFP": ["🎶 음악가", "🎨 디자이너", "📸 사진작가"],
    "ESTJ": ["📋 프로젝트 매니저", "🏭 기업 관리자", "📈 투자 분석가"],
}

# 🌟 헤더
st.markdown(
    """
    <h1 style='text-align: center; color: #FF6F61;'>🌟 MBTI 기반 진로 추천 🌟</h1>
    <p style='text-align: center; font-size:20px;'>당신의 성격유형에 맞는 멋진 직업을 찾아보세

