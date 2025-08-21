import streamlit as st

# MBTI별 추천 직업 데이터
career_dict = {
    "INTJ": ["전략 컨설턴트", "데이터 분석가", "연구원"],
    "ENTP": ["기업가", "마케팅 기획자", "스타트업 창업자"],
    "ESFP": ["이벤트 플래너", "연예인 매니저", "홍보 담당자"],
    "INFJ": ["상담가", "작가", "교사"],
  
}

st.title("MBTI 기반 진로 추천 웹 앱 🎯")

# MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    list(career_dict.keys())
)
