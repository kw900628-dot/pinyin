import streamlit as st
from pypinyin import pinyin, Style

st.set_page_config(page_title="중국어 병음 변환기", layout="wide")

st.title("🇨🇳 중국어 병음 변환기")

text_input = st.text_area(
    "중국어 텍스트 입력:",
    height=200,
    placeholder="여기에 중국어를 입력하세요 (예: 你好)"
)

if st.button("병음 변환하기"):
    if text_input:
        # ---------------------------------------------------------
        # [핵심] style=Style.TONE 옵션이 'ni3'를 'nǐ'로 바꿔줍니다.
        # ---------------------------------------------------------
        result_list = pinyin(text_input, style=Style.TONE)
        
        # 리스트를 문자열로 합치기
        converted_text = ' '.join([item[0] for item in result_list])
        
        st.success("변환 완료!")
        st.subheader("결과")
        st.code(converted_text, language=None)
    else:
        st.warning("텍스트를 입력해주세요.")