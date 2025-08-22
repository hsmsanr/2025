import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🔥 분야별 유행 트렌드 분석", layout="wide")

# ------------------ 샘플 데이터 ------------------
categories = {
    "음식": ["제로콜라", "일본 라멘", "하이볼", "헬스 보충제", "몬스터 에너지"],
    "패션": ["크록스", "슬리퍼 패션", "오버핏 셔츠", "버킷햇", "샌들"],
    "밈": ["진또배기 밈", "묵직하다 밈", "갓생 밈", "광고송 패러디", "AI 패러디"],
    "인물": ["프롬프트 엔지니어", "AI 유튜버", "아이돌 X", "e스포츠 선수", "웹소설 작가"],
    "기타": ["전동 킥보드", "캠핑용품", "드론 촬영", "스마트홈 기기", "AR 안경"]
}

# 각 항목에 점수 부여 (검색량/판매량/인기도 평균)
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
st.write("각 분야별로 현재 가장 유행하는 아이템들을 보여줍니다!"
