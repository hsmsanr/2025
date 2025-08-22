import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="🔥 요즘 뭐가 유행할까?", layout="wide")

# ------------------ 샘플 데이터 ------------------
data = {
    "항목": ["제로콜라", "크록스", "슬리퍼 패션", "오버핏 셔츠", "프롬프트 엔지니어", "몬스터 에너지", "진또배기 밈", "일본 라멘", "헬스 보충제", "하이볼"],
    "검색량": [random.randint(50, 100) for _ in range(10)],
    "판매량": [random.randint(50, 100) for _ in range(10)],
    "인기도": [random.randint(50, 100) for _ in range(10)],
}

df = pd.DataFrame(data)

# ------------------ 제목 ------------------
st.title("✨ 요즘 뜨는 트렌드 분석기")
st.write("검색량, 판매량, 인기도 데이터를 기반으로 **지금 유행하는 것들**을 확인해보세요!")

# ------------------ 인기 TOP 3 ------------------
st.subheader("🔥 지금 가장 핫한 TOP 3")
df["종합점수"] = df[["검색량", "판매량", "인기도"]].mean(axis=1)
top3 = df.sort_values("종합점수", ascending=False).head(3)

for i, row in top3.iterrows():
    st.markdown(f"### 🏆 {row['항목']}  —  점수: {row['종합점수']:.1f}")

# ------------------ 데이터 시각화 ------------------
st.subheader("📊 트렌드 지표 비교")
selected = st.multiselect("비교하고 싶은 항목을 선택하세요:", df["항목"].tolist(), default=top3["항목"].tolist())

if selected:
    fig, ax = plt.subplots()
    df_selected = df[df["항목"].isin(selected)]
    df_selected.set_index("항목")["검색량","판매량","인기도"].plot(kind="bar", ax=ax)
    st.pyplot(fig)

# ------------------ 상세 추천 ------------------
st.subheader("💡 트렌드 분석 및 추천")
choice = st.selectbox("관심 있는 분야를 골라보세요:", ["음식", "패션", "밈", "인물", "기타"])

if choice == "음식":
    st.success("🍜 요즘 라멘, 하이볼 같은 **일본식 음식과 주류**가 크게 뜨고 있어요!")
elif choice == "패션":
    st.success("👟 슬리퍼 패션, 오버핏 셔츠가 여름철 핫 아이템이에요!")
elif choice == "밈":
    st.success("😂 '진또배기' 같은 짧고 중독성 강한 밈이 대세!")
elif choice == "인물":
    st.success("🤖 '프롬프트 엔지니어' 같은 AI 관련 직업이 뜨는 중!")
else:
    st.info("📈 다양한 트렌드가 동시에 확산 중이니, 복합적인 관심사가 유리해요!")

# ------------------ 데이터 테이블 ------------------
st.subheader("📋 원본 데이터")
st.dataframe(df)

