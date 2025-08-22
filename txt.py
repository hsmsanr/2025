import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🔥 맞춤형 유행 트렌드", layout="wide")

# ------------------ 사용자 입력 ------------------
st.sidebar.title("✨ 나의 정보 입력")
age_group = st.sidebar.selectbox("연령대 선택", ["10대","20대","30대 이상"])
environment = st.sidebar.selectbox("주변 환경 선택", ["학생","직장인","주부","기타"])
interests = st.sidebar.multiselect("관심사 선택", ["음식","패션","밈","인물","기타"], default=["음식","패션"])
mood = st.sidebar.selectbox("현재 기분/분위기 선택", ["즐거움","편안함","자극","힐링","학습"])

# ------------------ 데이터 ------------------
categories = {
    "🍔 음식": {
        "제로콜라": {"desc":"저칼로리 열풍과 건강 트렌드", "age":["10대","20대"], "env":["학생","직장인"], "interests":["음식"], "mood":["즐거움","편안함"]},
        "하이볼": {"desc":"가볍게 즐기는 술로 인기", "age":["20대","30대 이상"], "env":["직장인"], "interests":["음식"], "mood":["자극"]},
        "일본 라멘": {"desc":"SNS 음식 리뷰로 유행", "age":["10대","20대"], "env":["학생","직장인"], "interests":["음식"], "mood":["즐거움"]},
        "헬스 보충제": {"desc":"운동 열풍으로 수요 증가", "age":["20대","30대 이상"], "env":["직장인"], "interests":["음식"], "mood":["자극"]},
        "몬스터 에너지": {"desc":"게이머·운동인 중심 확산", "age":["10대","20대"], "env":["학생","직장인"], "interests":["음식"], "mood":["자극"]}
    },
    "👗 패션": {
        "크록스": {"desc":"편리함과 꾸안꾸 스타일", "age":["10대","20대"], "env":["학생","직장인"], "interests":["패션"], "mood":["편안함"]},
        "슬리퍼 패션": {"desc":"여름철 편한 스타일", "age":["10대","30대 이상"], "env":["학생","주부"], "interests":["패션"], "mood":["편안함"]},
        "오버핏 셔츠": {"desc":"힙한 감성", "age":["20대"], "env":["직장인"], "interests":["패션"], "mood":["자극"]},
        "버킷햇": {"desc":"레트로+스트릿 패션", "age":["10대","20대"], "env":["학생","직장인"], "interests":["패션"], "mood":["즐거움"]},
        "샌들": {"desc":"여름철 필수템", "age":["20대","30대 이상"], "env":["직장인","주부"], "interests":["패션"], "mood":["편안함"]}
    },
    "🤣 밈": {
        "진또배기 밈": {"desc":"중독성 강한 멜로디", "age":["10대","20대"], "env":["학생","직장인"], "interests":["밈"], "mood":["즐거움"]},
        "묵직하다 밈": {"desc":"게임·스포츠 패러디", "age":["20대"], "env":["직장인"], "interests":["밈"], "mood":["자극"]},
        "갓생 밈": {"desc":"자기관리 열풍", "age":["10대","20대"], "env":["학생","직장인"], "interests":["밈"], "mood":["학습","자극"]},
        "광고송 패러디": {"desc":"TV광고 영향", "age":["30대 이상"], "env":["주부"], "interests":["밈"], "mood":["편안함"]},
        "AI 패러디": {"desc":"합성 기술로 만든 밈", "age":["20대"], "env":["직장인"], "interests":["밈"], "mood":["자극"]}
    },
    "🌟 인물": {
        "이강인": {"desc":"아시안컵 활약으로 인기", "age":["10대","20대"], "env":["학생","직장인"], "interests":["인물"], "mood":["자극"]},
        "뉴진스 민지": {"desc":"K-POP 인기", "age":["10대","20대"], "env":["학생","직장인"], "interests":["인물"], "mood":["즐거움"]},
        "손흥민": {"desc":"EPL 활약과 SNS 화제", "age":["20대"], "env":["직장인"], "interests":["인물"], "mood":["자극"]},
        "임영웅": {"desc":"트로트 인기", "age":["30대 이상"], "env":["주부"], "interests":["인물"], "mood":["편안함"]},
        "아이유": {"desc":"드라마·음원 인기", "age":["20대","30대 이상"], "env":["직장인","주부"], "interests":["인물"], "mood":["즐거움"]}
    },
    "💡 기타": {
        "전동 킥보드": {"desc":"도심 이동 수단", "age":["10대","20대"], "env":["학생","직장인"], "interests":["기타"], "mood":["즐거움","편안함"]},
        "캠핑용품": {"desc":"야외활동 증가", "age":["20대","30대 이상"], "env":["직장인","주부"], "interests":["기타"], "mood":["편안함"]},
        "드론 촬영": {"desc":"SNS 영상 제작", "age":["10대","20대"], "env":["학생","직장인"], "interests":["기타"], "mood":["즐거움"]},
        "스마트홈 기기": {"desc":"IoT 기술 발전", "age":["20대","30대 이상"], "env":["직장인","주부"], "interests":["기타"], "mood":["편안함"]},
        "AR 안경": {"desc":"메타버스 열풍", "age":["20대"], "env":["직장인"], "interests":["기타"], "mood":["즐거움"]}
    }
}

# ------------------ 점수 생성 ------------------
all_data = []
for cat, items in categories.items():
    for item, info in items.items():
        if age_group in info["age"] and environment in info["env"] and any(i in interests for i in info["interests"]) and mood in info["mood"]:
            종합점수 = random.randint(50,100)
            all_data.append([cat, item, info["desc"], 종합점수])

df = pd.DataFrame(all_data, columns=["분야","항목","설명","종합점수"])

# ------------------ 페이지 제목 ------------------
st.title("✨ 맞춤형 유행 트렌드 분석")
st.markdown(f"**연령대:** {age_group}, **환경:** {environment}, **관심사:** {', '.join(interests)}, **심정:** {mood}")

if df.empty:
    st.warning("해당 조건에 맞는 트렌드가 없습니다. 관심사나 심정을 조정해보세요!")
else:
    # ------------------ 분야별 TOP5 ------------------
    for cat in categories.keys():
        df_cat = df[df["분야"]==cat].sort_values("종합점수", ascending=False).head(5)
        if not df_cat.empty:
            st.subheader(f"{cat} 분야 TOP5 🔥")
            for i, row in df_cat.iterrows():
                rank = df_cat.index.get_loc(i) + 1
                st.markdown(
                    f"""
                    <div style="background-color:#f9f9f9; padding:12px; margin:6px; border-radius:12px; 
                                box-shadow:2px 2px 6px rgba(0,0,0,0.1);">
                        <h4>🏅 {rank}위: <b>{row['항목']}</b> ({row['종합점수']}점)</h4>
                        <p style="color:#555;">{row['설명']}</p>
                    </div>
                    """, unsafe_allow_html=True
                )
            # ------------------ 막대그래프 작게 표시 ------------------
            st.bar_chart(df_cat.set_index("항목")["종합점수"], height=200)
