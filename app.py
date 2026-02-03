import streamlit as st
from g2pM import G2pM

# 페이지 설정
st.set_page_config(page_title="고성능 중국어 병음 변환기", layout="wide")

st.title("🇨🇳 고성능 AI 병음 변환기 (g2pM)")
st.info("AI 모델을 사용하여 문맥에 맞는 정확한 성조를 찾아냅니다.")

# 1. 모델 로드 (캐싱을 통해 속도 최적화)
@st.cache_resource
def load_model():
    # 모델 초기화 (최초 1회 실행 시 시간이 조금 걸림)
    return G2pM()

try:
    model = load_model()
except Exception as e:
    st.error(f"모델 로드 중 오류 발생: {e}")

# 2. 텍스트 입력
text_input = st.text_area(
    "중국어 텍스트 입력:",
    height=200,
    placeholder="예: 银行 (은행 - yínháng) / 行走 (걷다 - xíngzǒu) - 같은 글자도 문맥에 따라 구분합니다."
)

if st.button("변환하기"):
    if text_input:
        with st.spinner("AI가 분석 중입니다..."):
            # tone=True: 성조 표시, char_split=False: 단어 단위 유지 시도
            pinyin_list = model(text_input, tone=True, char_split=False)
            
            # 리스트 결과를 문자열로 변환
            converted_text = " ".join(pinyin_list)
            
            st.success("변환 완료!")
            st.subheader("결과")
            st.code(converted_text, language=None)
    else:
        st.warning("텍스트를 입력해주세요.")