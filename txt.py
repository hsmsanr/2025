import streamlit as st
import pandas as pd
import random
import plotly.express as px

st.set_page_config(page_title="🔥 분야별 유행 트렌드 분석", layout="wide")

# ------------------ 샘플 데이터 ------------------
categories = {
    "음식": ["제로콜라", "일본 라멘", "하이볼", "헬스 보충제", "몬스터 에너지"],
    "패션": ["크록스", "슬리퍼 패션", "오버핏 셔츠", "버킷햇", "샌들"],
    "밈": ["진또배기 밈", "묵직하다 밈", "갓생 밈", "광고송 패러디", "AI 패러디"],
    "인물": ["프롬프트 엔지니어", "AI 유튜버", "아이돌 X", "e스포츠 선수", "웹소설 작가"],
    "기타": ["전동 킥보드", "캠핑용품", "드론 촬영", "스마트홈 기기", "AR 안경"]
}

# 점수 데이터 생성
all_data = []
for cat, items in categories.items():
    for item in items:
        검색량 = random.randint(50, 100)
        판매량 = random.randint(50, 100)
        인기도 = random.randint(50, 100)
        종합점수 = (검색량 + 판매량 + 인기도) / 3
        all_data.append([cat, item, 검색량, 판매량, 인기도, 종합점수])

df = pd.DataFrame(all_data, columns=["분야", "항목", "검색량", "판매량", "인기도", "종합점수"])

# ------------------ 제목 ------------------
st.title("✨ 분야별 요즘 뜨는 트렌드 TOP 5")
st.write("각 분야별로 현재 가장 유행하는 아이템들을 보여줍니다! (인터랙티브 그래프 🔥)")

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
    fig.update_layout(yaxis=dict(title="점수", showgrid=False), xaxis=dict(title="항목"))
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df_cat[["항목", "종합점수"]])

# ------------------ 각 분야 1위만 모아보기 ------------------
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
fig_top1.update_layout(yaxis=dict(title="점수", showgrid=False))
st.plotly_chart(fig_top1, use_container_width=True)

st.dataframe(top1[["분야", "항목", "종합점수"]])

