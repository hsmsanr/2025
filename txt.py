import streamlit as st

# -----------------------
# 샘플 트렌드 데이터
# -----------------------
trends = {
    "인물": [
        {"name": "아이유", "desc": "음악과 드라마에서 활약하며 꾸준한 인기 유지", "age": ["10대","20대","30대"], "env": ["도시","학교","교외"], "interest": ["음악","연예인"]},
        {"name": "손흥민", "desc": "프리미어리그 활약으로 전世대적 인기", "age": ["10대","20대","30대","40대"], "env": ["도시","교외"], "interest": ["스포츠"]},
        {"name": "뉴진스", "desc": "신선한 음악과 스타일로 Z세대 아이콘", "age": ["10대","20대"], "env": ["학교","도시"], "interest": ["음악","패션"]},
        {"name": "이강인", "desc": "축구 스타로 급부상", "age": ["10대","20대"], "env": ["도시","학교"], "interest": ["스포츠"]},
        {"name": "유재석", "desc": "국민MC로 꾸준한 예능계 인기", "age": ["20대","30대","40대"], "env": ["도시","교외"], "interest": ["예능"]}
    ],
    "음식": [
        {"name": "마라탕", "desc": "중독성 강한 맛으로 젊은 층 인기", "age": ["10대","20대"], "env": ["도시","학교"], "interest": ["음식"]},
        {"name": "크로플", "desc": "카페 디저트로 SNS 인기", "age": ["10대","20대","30대"], "env": ["도시","학교"], "interest": ["음식"]},
        {"name": "떡볶이", "desc": "대한민국 대표 길거리 음식", "age": ["10대","20대","30대"], "env": ["학교","도시"], "interest": ["음식"]},
        {"name": "샐러드", "desc": "건강식으로 MZ세대 관심 증가", "age": ["20대","30대"], "env": ["도시","교외"], "interest": ["음식","건강"]},
        {"name": "삼겹살", "desc": "국민 고기 메뉴, 전世대적 인기", "age": ["10대","20대","30대","40대"], "env": ["도시","교외","학교"], "interest": ["음식"]}
    ],
    "패션": [
        {"name": "크록스", "desc": "편리함과 꾸안꾸 패션으로 자리잡음", "age": ["10대","20대"], "env": ["학교","도시"], "interest": ["패션"]},
        {"name": "와이드팬츠", "desc": "힙한 분위기로 10대~20대 유행", "age": ["10대","20대"], "env": ["도시","학교"], "interest": ["패션"]},
        {"name": "뉴발란스 운동화", "desc": "편안함과 레트로 감성으로 인기", "age": ["10대","20대","30대"], "env": ["도시","교외"], "interest": ["패션"]},
        {"name": "트레이닝 셋업", "desc": "편한 스타일을 중시하는 꾸안꾸 트렌드", "age": ["10대","20대","30대"], "env": ["학교","도시"], "interest": ["패션"]},
        {"name": "야구 모자", "desc": "데일리룩 필수 아이템", "age": ["10대","20대","30대"], "env": ["도시","학교"], "interest": ["패션"]}
    ],
    "밈": [
        {"name": "진또배기", "desc": "흥겨운 멜로디와 밈으로 급부상", "age": ["10대","20대"], "env": ["학교","도시"], "interest": ["밈","음악"]},
        {"name": "오마에와 모 신데이루", "desc": "애니 대사로 유행", "age": ["10대","20대"], "env": ["학교","도시"], "interest": ["밈"]},
        {"name": "킹받네", "desc": "신조어 밈으로 널리 사용", "age": ["10대","20대"], "env": ["학교","도시"], "interest": ["밈"]},
        {"name": "짤랑이 짤", "desc": "커뮤니티 중심으로 확산", "age": ["10대","20대","30대"], "env": ["도시","학교"], "interest": ["밈"]},
        {"name": "이게 나라냐", "desc": "풍자와 밈으로 쓰임", "age": ["20대","30대"], "env": ["도시","교외"], "interest": ["밈"]}
    ]
}

# -----------------------
# UI
# -----------------------
st.title("🔥 요즘 트렌드 추천 웹앱")

st.sidebar.header("사용자 정보 입력")

age = st.sidebar.selectbox("연령대", ["선택하세요","10대","20대","30대","40대"])
env = st.sidebar.selectbox("주변환경", ["선택하세요","도시","교외","학교"])
interest = st.sidebar.selectbox("관심사", ["선택하세요","음악","스포츠","패션","음식","밈","연예인","예능","건강"])
mood = st.sidebar.selectbox("심정/분위기", ["선택하세요","힙하게","밝게","편안하게","집중하고 싶음"])

# -----------------------
# 추천 로직
# -----------------------
if age != "선택하세요" and env != "선택하세요" and interest != "선택하세요" and mood != "선택하세요":
    st.subheader(f"✨ {age}, {env}, 관심: {interest}, 분위기: {mood} → 맞춤 트렌드 TOP5")

    for category, items in trends.items():
        # 조건과 맞는 데이터 우선 선택
        filtered = [i for i in items if age in i["age"] and env in i["env"] and interest in i["interest"]]

        # 5개 미만이면 같은 분야에서 채워서 보충
        if len(filtered) < 5:
            extra = [i for i in items if i not in filtered]
            filtered += extra[:5 - len(filtered)]

        # 5개 이상이면 상위 5개만
        final_items = filtered[:5]

        # 분야 제목 출력
        st.markdown(f"#### 📌 {category} TOP5")

        # 세로 막대그래프 (Streamlit 기본)
        st.bar_chart([1]*len(final_items), x=[i["name"] for i in final_items])

        # 설명 출력
        for i, trend in enumerate(final_items, start=1):
            st.write(f"**{i}. {trend['name']}** - {trend['desc']}")

else:
    st.info("👆 왼쪽 사이드바에서 모든 정보를 입력하세요!")
