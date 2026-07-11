import streamlit as st

st.set_page_config(
    page_title="나의 취미 소개",
    page_icon="🎯",
    layout="wide"
)

# =======================
# CSS 디자인
# =======================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom, #0f172a, #1e293b);
    color: white;
}

h1{
    color:#FFD166;
    text-align:center;
}

h2,h3{
    color:#FFD166;
}

div.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

[data-testid="stSidebar"]{
    background-color:#111827;
}

.stButton>button{
    background-color:#FFD166;
    color:black;
    border-radius:10px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =======================
# 메인 화면
# =======================

st.title("🎯 나의 취미 소개")

st.write("---")

st.header("안녕하세요! 👋")

st.write("""
이 웹사이트는 **저의 취미를 소개하기 위해 만든 Streamlit 프로젝트**입니다.

저는 다양한 취미를 가지고 있으며,
그중에서도 가장 좋아하는 취미 세 가지를 소개하고자 합니다.

왼쪽 사이드바에서 원하는 페이지를 선택해 주세요.
""")

st.write("### 📚 소개할 취미")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### ⚾ 야구

- 가장 좋아하는 팀
- 좋아하는 선수
- 야구의 매력
""")

with col2:
    st.markdown("""
### 📚 독서

- What If?
- 랜들 먼로
- 과학 이야기
""")

with col3:
    st.markdown("""
### 🧩 큐브

- 3×3 큐브
- 최고 기록 18초
- GAN Cube
""")

st.write("---")

st.info("💡 왼쪽 메뉴에서 페이지를 선택하여 각 취미를 자세히 살펴보세요!")

st.caption("Made with ❤️ using Streamlit")
