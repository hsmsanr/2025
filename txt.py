import streamlit as st
import pandas as pd
import random
import plotly.express as px

st.set_page_config(page_title="🔥 분야별 유행 트렌드 분석", layout="wide")

# ------------------ 데이터 (분야별 항목 + 설명) ------------------
categories = {
    "음식": {
        "제로콜라": "저칼로리 열풍과 건강 트렌드 덕분에 인기 상승",
        "일본 라멘": "일본식 음식 전문점 확산과 SNS 음식 리뷰로 유행",
        "하이볼": "젊은 층에서 가볍게 즐길 수 있는 술로 인기",
        "헬스 보충제": "운동 열풍과 헬스장 붐으로 수요 증가",
        "몬스터 에너지": "게이머와 운동인을 중심으로 확산"
    },
    "패션": {
        "크록스": "편리함과 꾸안꾸 패션 아이템으로 자리잡음",
        "슬리퍼 패션": "여름철 편한 스타일이 Z세대에게 인기",
        "오버핏 셔츠": "체형 커버 + 힙한 감성으로 유행",
        "버킷햇": "레트로 감성과 스트릿 패션에서 재조명",
        "샌들": "여름철 필수템으로 다양한 브랜드 출시"
    },
    "밈": {
        "진또배기 밈": "중독성 강한 멜로디와 짧은 영상으로 확산",
        "묵직하다 밈": "게임·스포츠 장면에서 패러디로 사용",
        "갓생 밈": "자기관리 열풍을 표현하는 Z세대 단어",
        "광고송 패러디": "TV광고 멜로디가 온라인에서 유행",
        "AI 패러디": "AI 합성 기술로 만든 밈이 폭발적 인기"
    },
    "인물": {
        "이강인": "아시안컵과 유럽 리그 활약으로 인기 급상승",
        "뉴진스 민지": "K-POP 글로벌 인기와 패션 아이콘으로 주목",
        "손흥민": "EPL 활약과 SNS 화제성으로 꾸준히 인기",
        "임영웅": "트로트 열풍과 충성 팬덤으로 높은 지지",
        "아이유": "드라마·음원 활동 동시 인기"
    },
    "기타": {
        "전동 킥보드": "도심 이동 수단으로 자리잡음",
        "캠핑용품": "야외활동 증가로 꾸준한 수요",
        "드론 촬영": "SNS·유튜브 영상 콘텐츠 제작에 활용",
        "스마트홈 기기": "편리한 생활과 IoT 기술 발전",
        "AR 안경": "메타버스·증강현실 열풍으로 관심 증가"
    }
}

# ------------------ 점수 생성 ------------------
all_data = []
for cat, items in categories.items():
    for item, desc in items.items():
        검색량 = random.randint(50, 100)
        판매량 = random.randint(50, 100)
        인기도 = random.randint(50, 100)
        종합점수 = (검색량 + 판매량 + 인기도) / 3
        all_data.append([cat, item, desc, 검색량, 판매량, 인기도, 종합점수])

df = pd.DataFrame(all_data, columns=["분야", "항목", "설명", "검색량", "판매량", "인기도", "종합점수"])

# ------------------ 제목 ------------------
st.title("✨ 분야별 요즘 뜨는 트렌드 TOP 5")
st.write("각 분야별로 현재 가장 유행하는 아이템과 그 이유를 보여줍니다!")

# ------------------ 분야별 TOP 5 ------------------
for cat in categories.keys():
    st.subheader(f"🔥 {cat} 분야 TOP 5")
    df_cat = df[df["분야"] == cat].sort_values("종합점수", ascending=False).head(5)
    
    fig = px.bar(
        df_cat, 
        x="항목", 
        y="종합점수", 
        color="항목",
        text="종합점수",
        title=f"{cat} 분야 TOP 5",
        template="plotly_white"
    )
    fig.update_traces(textposition="outside", marker=dict(line=dict(width=1, color="black")))
    st.plotly_chart(fig, use_container_width=True)
    
    # 설명 표
    st.dataframe(df_cat[["항목", "설명", "종합점수"]])

# ------------------ 각 분야 1위 모아보기 ------------------
st.subheader("🏆 각 분야별 1위 아이템 모아보기")
top1 = df.sort_values("종합점수", ascending=False).groupby("분야").head(1)

fig_top1 = px.bar(
    top1,
    x="분야",
    y="종합점수",
    color="항목",
    text="항목",
    title="분야별 1위 비교",
    template="plotly_white"
)
fig_top1.update_traces(textposition="inside", marker=dict(line=dict(width=1, color="black")))
st.plotly_chart(fig_top1, use_container_width=True)

st.dataframe(top1[["분야", "항목", "설명", "종합점수"]])
