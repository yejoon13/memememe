import streamlit as st

st.set_page_config(page_title="좋아하는 야구", page_icon="⚾")

st.title("⚾ 내가 좋아하는 야구")

st.image("images/baseball.jpg", use_container_width=True)

st.header("야구를 좋아하는 이유")

st.write("""
저는 야구를 보는 것을 정말 좋아합니다.

야구는 경기의 흐름이 계속 바뀌고 마지막까지 결과를 예측하기 어려워 더욱 재미있습니다.
선수들의 멋진 수비와 시원한 홈런, 그리고 팬들과 함께 응원하는 분위기도 야구의 큰 매력이라고 생각합니다.
""")

st.header("❤️ 내가 가장 좋아하는 팀")

st.success("KIA 타이거즈")

st.write("""
제가 가장 좋아하는 팀은 **KIA 타이거즈**입니다.

KIA 타이거즈 선수들의 열정적인 플레이를 보는 것을 좋아하며,
특히 투수 **양현종 선수**를 가장 좋아합니다.
오랫동안 팀을 위해 활약하는 모습과 뛰어난 투구 실력,
그리고 중요한 경기에서도 흔들리지 않는 모습이 정말 멋지다고 생각합니다.
""")

st.header("⚾ 야구의 매력")

st.markdown("""
- ⚾ 짜릿한 홈런
- 🧤 멋진 수비
- 🏃 다양한 작전과 전략
- 📣 응원 문화
- 🏆 끝까지 알 수 없는 경기 결과
""")
