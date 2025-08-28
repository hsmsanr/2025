import streamlit as st
import matplotlib.pyplot as plt

# ---------------------------
# 트렌드 데이터 예시
# ---------------------------
trends = {
    "10대": {
        "패션": [
            {"이름": "크록스", "설명": "편리함과 꾸안꾸 패션으로 자리잡음"},
            {"이름": "카고바지", "설명": "힙하고 편안한 스타일로 인기를 얻음"},
            {"이름": "뉴진스 스타일", "설명": "아이돌 패션이 유행을 선도"},
            {"이름": "와이드 팬츠", "설명": "편안함과 트렌디함을 동시에 추구"},
            {"이름": "크롭티", "설명": "여름철 패션 아이템으로 자리매김"}
        ],
        "음식": [
            {"이름": "마라탕", "설명": "중국식 얼얼한 매운맛으로 인기"},
            {"이름": "분식 배달", "설명": "간편하면서 가성비 좋은 한 끼"},
            {"이름": "대왕 돈가스", "설명": "인스타 인증샷 음식으로 인기"},
            {"이름": "빙수", "설명": "여름철 대표 디저트로 부상"},
            {"이름": "떡볶이 퓨전", "설명": "이색 조합으로 SNS에서 화제"}
        ],
        "밈/유행어": [
            {"이름": "진또배기", "설명": "밈으로 퍼지며 다양한 패러디 유행"},
            {"이름": "갓생살기", "설명": "자기계발 열풍을 반영"},
            {"이름": "스불재", "설명": "스스로 불러온 재앙을 뜻하며 공감대 형성"},
            {"이름": "킹받네", "설명": "화날 때 쓰는 유머러스한 표현"},
            {"이름": "당근이세요?", "설명": "중고거래 플랫폼에서 유래"}
        ],
        "인물": [
            {"이름": "뉴진스", "설명": "10대 문화를 선도하는 아이돌 그룹"},
            {"이름": "아이브", "설명": "세련된 이미지와 음악으로 인기"},
            {"이름": "손흥민", "설명": "국민적인 스포츠 스타"},
            {"이름": "임영웅", "설명": "세대를 아우르는 가수"},
            {"이름": "안유진", "설명": "예능과 음악에서 두각을 나타냄"}
        ]
    }
}

# ---------------------------
# 예쁜 바 차트 그리기 함수
# ---------------------------
def draw_bar_chart(data, title):
    names = [d["이름"] for d in data]
    values = list(range(len(data), 0, -1))  # 5,4,3,2,1 랭킹 값
    
    colors = plt.cm.Paired(range(len(data)))  # 다양한 색상 팔레트 적용
    
    fig, ax = plt.subplots(figsize=(5, 3))  # 크기 작게
    bars = ax.bar(names, values, color=colors, width=0.6)
    
    # 제목 & 라벨
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_ylabel("인기 순위", fontsize=10)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=20, ha="right", fontsize=9)
    ax.set_yticks(range(1, len(data)+1))
    ax.set_yticklabels(list(range(5, 0, -1)))  # 1위~5위
    
    # 각 막대 위에 순위 표시
    for bar, rank in zip(bars, range(1, len(data)+1)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f"{rank}위",
                ha='center', va='bottom', fontsize=9, fontweight="bold")
    
    st.pyplot(fig)

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="최신 트렌드 TOP5", layout="centered")

st.title("✨ 나에게 맞는 최신 트렌드 TOP 5 ✨")

# 사용자 입력
age = st.selectbox("연령대 (선택하세요)", ["선택하세요", "10대", "20대", "30대 이상"])
interest = st.selectbox("관심 분야 (선택하세요)", ["선택하세요", "패션", "음식", "밈/유행어", "인물"])

if age != "선택하세요" and interest != "선택하세요":
    if age in trends and interest in trends[age]:
        data = trends[age][interest][:5]  # 5개만 가져오기
        st.subheader(f"📌 {age}의 {interest} 트렌드 TOP 5")
        
        # 설명 리스트 출력
        for idx, item in enumerate(data, 1):
            st.markdown(f"**{idx}위. {item['이름']}** - {item['설명']}")
        
        # 그래프 출력
        draw_bar_chart(data, f"{interest} TOP 5")
    else:
        st.warning("해당 조건에 맞는 트렌드 데이터가 부족합니다.")
else:
    st.info("연령대와 관심 분야를 모두 선택하세요.")
