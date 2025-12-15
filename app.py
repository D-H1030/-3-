import streamlit as st

# 웹 페이지 기본 설정
st.set_page_config(
    page_title = "C311014 권도화",
    page_icon = "icon/free-icon-monkey-2772411.png",
    layout = "centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help' : "https://docs.streamlit.io",
        "Report a bug" : "https://streamlit.io",
        'About' : "나 - 홍익대학교 컴퓨터공학과 3학년"
    }
)


st.title('C311014 권도화')
st.divider()

st.write('### K팝 데몬 헌터스 팬덤 형성의 핵심 요인 분석')

st.write('\n\n')

'''
[k팝 데몬 헌터스 알아보기]
'''
st.link_button("k팝 데몬 헌터스(나무위키)", "https://namu.wiki/w/%EC%BC%80%EC%9D%B4%ED%8C%9D%20%EB%8D%B0%EB%AA%AC%20%ED%97%8C%ED%84%B0%EC%8A%A4")

st.write('\n\n')

st.write('#### 1. k팝 데몬 헌터스 관련 뉴스 단어 워드클라우드')
st.image('k-pop demon hunters wordcloud.png', use_container_width=True)
'''
위의 워드클라우드를 보면, 케데헌이 전세계적으로 열풍을 일으킨 요인으로
다음 세 가지를 볼 수 있을 것 같다. 

1) 사운드 트랙
2) 연출
3) 소재

'''

st.divider()

st.write('\n\n')
st.write('#### 2. k팝 데몬 헌터스 관련 뉴스 단어 네트워크 시각화')
st.image('network1.png', use_container_width=True)
st.image('network2.png', use_container_width=True)

ballon_snow_button = st.button('풍선과 눈을 내려 보세요')
if ballon_snow_button:
    st.balloons()
    st.snow()
