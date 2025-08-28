import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="트렌드 추천 앱", page_icon="🔥", layout="centered")

st.title("✨ 나에게 맞는 요즘 트렌드 ✨")
st.write("연령대, 환경, 관심사, 심정을 입력하면 당신에게 맞는 트렌드를 보여드려요!")

# -------------------------------
# 선택지 입력
# -------------------------------
age_group = st.selectbox("연령대 (선택하세요)", ["선택하세요", "10대", "20대", "30대 이상"])
environment = st.selectbox("주변 환경 (선택하세요)", ["선택하세요", "도시", "교외", "학교", "직장"])
interest = st.selectbox("관심사 (선택하세요)", ["선택하세요", "패션", "음식", "게임", "밈/유행어", "학교생활"])
mood = st.selectbox("현재 심정 (선택하세요)", ["선택하세요", "힐링 필요", "스트레스 해소", "재미 찾는 중", "공부 집중"])

# -------------------------------
# 트렌드 데이터베이스 (예시)
# -------------------------------
trend_data = {
    "패션": [
        {"name": "크록스", "desc": "편리함과 꾸안꾸 패션으로 자리잡음"},
        {"name": "카고 팬츠", "desc": "실용성과 스타일을 동시에"},
        {"name": "빈티지 패션", "desc": "개성을 살리는 복고풍"},
        {"name": "뉴발란스", "desc": "편안함과 트렌디함"},
        {"name": "오버핏 셔츠", "desc": "자유로운 느낌 강조"}
    ],
    "음식": [
        {"name": "제로콜라", "desc": "MZ세대 필수템"},
        {"name": "마라탕", "desc": "중독성 강한 얼얼한 맛"},
        {"name": "떡볶이", "desc": "불변의 국민 간식"},
        {"name": "포케", "desc": "가벼운 건강식"},
        {"name": "편의점 도시락", "desc": "간편하고 가성비 좋음"}
    ],
    "게임": [
        {"name": "롤토체스", "desc": "전략적 두뇌 싸움"},
        {"name": "오버워치2", "desc": "팀플레이의 묘미"},
        {"name": "마인크래프트", "desc": "무궁무진한 창의력 발휘"},
        {"name": "배틀그라운드", "desc": "여전히 뜨거운 배틀로얄"},
        {"name": "쿠키런 킹덤", "desc": "귀엽고 중독성 강한 게임"}
    ],
    "밈/유행어": [
        {"name": "진또배기 밈", "desc": "중독성 강한 유행 밈"},
        {"name": "삼쩜삼", "desc": "절세와 환급 서비스로 화제"},
        {"name": "개이득", "desc": "득템의 기쁨 표현"},
        {"name": "이게 나라냐", "desc": "풍자와 비판의 상징"},
        {"name": "킹받네", "desc": "분노와 귀여움 동시에"}
    ],
    "학교생활": [
        {"name": "스터디카페", "desc": "공부 집중 성지"},
        {"name": "갤럭시 탭 필기", "desc": "디지털 공부 툴"},
        {"name": "학교 축제 밴드부", "desc": "열정과 무대의 순간"},
        {"name": "동아리 활동", "desc": "자기계발과 네트워킹"},
        {"name": "급식 밈", "desc": "공감 백배 학교생활 유머"}
    ]
}

# -------------------------------
# 입력 조건에 맞는 트렌드 선택
# -------------------------------
if age_group != "선택하세요" and environment != "선택하세요" and interest != "선택하세요" and mood != "선택하세요":
    st.subheader("📊 당신을 위한 트렌드 추천")

    items = trend_data.get(interest, [])

    # 입력값 무관하게 최소 5개 출력 보장
    final_items = random.sample(items, k=min(5, len(items)))

    # 표 형식 출력
    for idx, item in enumerate(final_items, 1):
        st.markdown(f"**{idx}. {item['name']}** - {item['desc']}")

    # -------------------------------
    # 막대그래프 (세로, 작게, 예쁘게)
    # -------------------------------
    df = pd.DataFrame({
        "항목": [i["name"] for i in final_items],
        "인기도 점수": [len(final_items) - idx for idx, _ in enumerate(final_items)]
    })

    st.bar_chart(df, x="항목", y="인기도 점수", use_container_width=True)

else:
    st.info("⬆️ 모든 항목을 선택하면 트렌드 결과가 나타납니다.")
