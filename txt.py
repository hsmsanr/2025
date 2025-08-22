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

# ------------------ 페이지 제목 ------------------
st.title("✨ 요즘 뜨는 트렌드 분석")
st.markdown("**분야별 TOP5 트렌드**와 함께, 간단한 설명/유행 원인까지 카드 스타일로 정리했어요!")

# ------------------ 분야별 TOP5 ------------------
for cat in categories.keys():
    st.subheader(f"{cat} 분야 TOP5 🔥")
    df_cat = df[df["분야"]==cat].sort_values("종합점수", ascending=False).head(5)

    # 카드 스타일 출력
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

    # 그래프 (보조 느낌)
    st.bar_chart(df_cat.set_index("항목")["종합점수"])

# ------------------ 각 분야별 1위만 모아보기 ------------------
st.subheader("🏆 각 분야별 1위 모음")
top1 = df.sort_values("종합점수", ascending=False).groupby("분야").head(1)
for i, row in top1.iterrows():
    st.markdown(f"**{row['분야']} 1위 → {row['항목']} ✨ ({row['설명']})**")


