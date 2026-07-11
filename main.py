import streamlit as st

st.set_page_config(
    page_title="나의 취미 소개",
    page_icon="🎯",
    layout="wide"
)

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>

.stApp{
    background-color:#FFFFFF;
}

/* 제목 */
h1{
    color:#1E3A8A;
    text-align:center;
    font-size:48px;
}

/* 소제목 */
h2,h3{
    color:#1E3A8A;
}

/* 일반 글씨 */
p, li{
    color:#333333;
    font-size:18px;
}

/* 사이드바 */
[data-testid="stSidebar"]{
    background-color:#F3F4F6;
}

/* 성공 메시지 */
[data-testid="stAlert"]{
    background-color:#E0F2FE;
}

/* 카드처럼 보이게 */
.card{
    background:#F8FAFC;
    padding:20px;
    border-radius:15px;
    border:1px solid #D1D5DB;
    box-shadow:2px 2px 8px rgba(0,0,0,0.08);
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# 메인 화면
# -------------------------

st.title("🎯 나의 취미 소개")

st.markdown("""
## 안녕하세요!

이 웹사이트는 **저의 취미를 소개하기 위해 만든 Streamlit 프로젝트**입니다.

저는 평소 다양한 취미를 즐기고 있으며, 그중 가장 좋아하는 세 가지를 소개하고자 합니다.

왼쪽 사이드바에서 원하는 페이지를 선택해 주세요.
""")

st.divider()

st.subheader("📖 소개할 취미")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class="card">

### ⚾ 야구

❤️ 좋아하는 팀

⭐ 좋아하는 선수

📣 야구의 매력

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">

### 📚 독서

📖 What If?

🧠 과학 이야기

💡 상상력과 호기심

</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="card">

### 🧩 큐브

🏆 최고 기록 : 18초

🎲 GAN Cube

🚀 다양한 큐브 연습

</div>
""", unsafe_allow_html=True)

st.divider()

st.info("👈 왼쪽 메뉴에서 페이지를 선택하여 각 취미를 자세히 살펴보세요!")

st.caption("Made with ❤️ using Streamlit")
