import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🔥 요즘 유행 트렌드", layout="wide")

# ------------------ 데이터 ------------------
categories = {
    "🍔 음식": {
        "제로콜라": "저칼로리 열풍과 건강 트렌드 덕분에 인기 상승",
        "일본 라멘": "SNS 음식 리뷰로 유행",
        "하이볼": "젊은 층에서 가볍게 즐길 수 있는 술",
        "헬스 보충제": "운동 열풍으로 수요 증가",
        "몬스터 에너지": "게이머·운동인 중심 확산"
    },
    "👗 패션": {
        "크록스": "편리함과 꾸안꾸 패션으로 자리잡음",
        "슬리퍼 패션": "여름철 편한 스타일로 인기",
        "오버핏 셔츠": "힙한 감성으로 유행",
        "버킷햇": "레트로+스트릿 패션에서 재조명",
        "샌들": "여름철 필수 아이템"
    },
    "🤣 밈": {
        "진또배기 밈": "중독성 강한 멜로디",
        "묵직하다 밈": "게임·스포츠 패러디 인기",
        "갓생 밈": "자기관리 열풍을 표현",
        "광고송 패러디": "TV광고 멜로디가 온라인 확산",
        "AI 패러디": "합성 기술로 만든 밈"
    },
    "🌟 인물": {
        "이강인": "아시안컵 활약으로 급상승",
        "뉴진스 민지": "K-POP 글로벌 인기",
        "손흥민": "EPL 활약과 SNS 화제",
        "임영웅": "트로트 열풍+팬덤",
        "아이유": "드라마·음원 동시 인기"
    },
    "💡 기타": {
        "전동 킥보드": "도심 이동 수단",
        "캠핑용품": "야외활동 증가",
        "드론 촬영": "SNS 영상 제작",
        "스마트홈 기기": "IoT 기술 발전",
        "AR 안경": "메타버스 열풍"
    }
}

# ------------------ 점수 생성 ------------------
all_data = []
for cat, items in categories.items():
    for item, desc in items.items():
        종합점수 = random.randint(50,100)
        all_data.append([cat, item, desc, 종합점수])
df = pd.DataFrame(all_data, columns=["분야","항목","설명","종합점수"])

# ------------------ 입력 UI ------------------
st.title("✨ 맞춤형 요즘 뜨는 트렌드 분석")

st.markdown("아래 정보를 입력하면, 당신에게 딱 맞는 **최신 트렌드 TOP5**를 보여드려요! 🚀")

col1, col2 = st.columns(2)
with col1:
    age = st.selectbox("연령대 (선택지: 선택하세요 ✨)", ["선택하세요", "10대", "20대", "30대", "40대 이상"])
    env = st.selectbox("주변환경 (선택지: 선택하세요 ✨)", ["선택하세요", "도시", "교외", "학교", "직장"])
with col2:
    interest = st.selectbox("관심사 (선택지: 선택하세요 ✨)", ["선택하세요", "음식", "패션", "밈", "인물", "기타"])
    mood = st.selectbox("현재 심정 (선택지: 선택하세요 ✨)", ["선택하세요", "즐거움", "피곤함", "힐링 필요", "자기계발", "유머 찾는 중"])

# ------------------ 필터링 ------------------
filtered_df = df.copy()

if age != "선택하세요":
    if age == "10대":  
        filtered_df = filtered_df[~filtered_df["항목"].isin(["하이볼","헬스 보충제"])]
    elif age == "40대 이상":
        filtered_df = filtered_df[~filtered_df["항목"].isin(["AI 패러디","버킷햇"])]

if interest != "선택하세요":
    filtered_df = filtered_df[filtered_df["분야"].str.contains(interest[0])]

if mood != "선택하세요":
    if mood == "유머 찾는 중":
        filtered_df = filtered_df[filtered_df["분야"]=="🤣 밈"]
    elif mood == "힐링 필요":
        filtered_df = filtered_df[filtered_df["분야"].isin(["🍔 음식","💡 기타"])]

# ------------------ 결과 ------------------
st.subheader("🎯 맞춤형 트렌드 TOP5")

if filtered_df.empty:
    st.warning("⚠️ 조건에 맞는 트렌드가 없어요! 선택지를 바꿔보세요.")
else:
    result = filtered_df.sort_values("종합점수", ascending=False).head(5)

    for i, row in result.iterrows():
        rank = result.index.get_loc(i) + 1
        st.markdown(
            f"""
            <div style="background-color:#f9f9f9; padding:12px; margin:6px; border-radius:12px; 
                        box-shadow:2px 2px 6px rgba(0,0,0,0.1); margin-bottom:10px;">
                <h4>🏅 {rank}위: <b>{row['항목']}</b> ({row['종합점수']}점)</h4>
                <p style="color:#555;">{row['설명']}</p>
            </div>
            """, unsafe_allow_html=True
        )

    st.bar_chart(result.set_index("항목")["종합점수"])
