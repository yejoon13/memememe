import streamlit as st

st.set_page_config(
    page_title="나의 취미 소개",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
    background-color:#1E293B;
    color:white;
}

h1,h2,h3{
    color:#FFD166;
}

[data-testid="stSidebar"]{
    background-color:#0F172A;
}
</style>
""", unsafe_allow_html=True)

st.title("🎯 나의 취미 소개")

st.write("""
안녕하세요!

이 사이트는 제가 좋아하는 취미를 소개하기 위해 만든 웹사이트입니다.

왼쪽 메뉴에서 원하는 페이지를 선택해 주세요.
""")

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("⚾ 야구")
    st.write("좋아하는 팀과 선수 소개")

with col2:
    st.subheader("📚 독서")
    st.write("가장 좋아하는 과학책 소개")

with col3:
    st.subheader("🧩 큐브")
    st.write("3×3 큐브 취미 소개")

st.success("👈 왼쪽 메뉴에서 페이지를 선택하세요!")
