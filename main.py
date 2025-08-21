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
    <p style='text-align: center; font-size:20px;'>당신의 성격유형에 맞는 멋진 직업을 찾아보세요! 🎯💼✨</p>
    """,
    unsafe_allow_html=True
)

# 🎲 랜덤 MBTI 버튼
if st.button("🎲 랜덤 MBTI 뽑기!"):
    mbti = random.choice(list(career_dict.keys()))
    st.success(f"오늘의 MBTI는... 🥁 {mbti} 입니다! 🎉")
else:
    # ✨ 드롭다운 선택
    mbti = st.selectbox("👉 당신의 MBTI를 선택하세요:", list(career_dict.keys()))

# 📌 추천 결과 출력
if mbti:
    st.subheader(f"✨ {mbti} 유형을 위한 추천 직업 ✨")
    st.markdown("💡 아래 직업들이 당신에게 딱 어울려요! 🌟")

    # 직업 리스트 출력
    for job in career_dict[mbti]:
        st.markdown(f"- {job}")

    # 🔮 특별 메시지
    st.info(f"🌟 {mbti} 유형은 특히 {career_dict[mbti][0]} 같은 분야에서 탁월한 능력을 발휘할 수 있어요! 🚀")

    # 🎨 화려한 구분선
    st.markdown("---")
    st.markdown("✨ 더 많은 가능성을 찾아보며 당신의 길을 개척하세요! 🌈💼🌍")
