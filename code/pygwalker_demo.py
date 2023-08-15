import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Streamlit 페이지의 너비 조정
st.set_page_config(
    page_title="Streamlit에서 Pygwalker 사용하기",
    layout="wide"
)
 
# 제목 추가
st.title("Streamlit에서 Pygwalker 사용하기")
 
# 데이터 가져오기
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
 
# Pygwalker를 사용하여 HTML 생성
pyg_html = pyg.walk(df, return_html=True)
 
# Streamlit 앱에 HTML 임베드
components.html(pyg_html, height=1000, scrolling=True)