# 필터링
filtered_data = []
for cat, items in categories.items():
    for item, info in items.items():
        score = 0
        if age_group in info["age"]:
            score += 30
        if environment in info["env"]:
            score += 30
        if any(i in interests for i in info["interests"]):
            score += 20
        if mood in info["mood"]:
            score += 20
        if score > 0:
            종합점수 = score + random.randint(0,20)
            filtered_data.append([cat, item, info["desc"], 종합점수])

df_filtered = pd.DataFrame(filtered_data, columns=["분야","항목","설명","종합점수"])

# 점수 순으로 상위 5개만
df_top = df_filtered.sort_values("종합점수", ascending=False).head(5)

# 출력
st.title("✨ 맞춤형 추천 트렌드")
for i, row in df_top.iterrows():
    st.markdown(
        f"""
        <div style="background-color:#f9f9f9; padding:12px; margin:6px; border-radius:12px; 
                    box-shadow:2px 2px 6px rgba(0,0,0,0.1);">
            <h4>🏅 {row['분야']} → <b>{row['항목']}</b> ({row['종합점수']}점)</h4>
            <p style="color:#555;">{row['설명']}</p>
        </div>
        """, unsafe_allow_html=True
    )
