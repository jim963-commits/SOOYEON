import streamlit as st
import os
from openai import OpenAI

# 환경 변수에서 API 키 읽기
client = OpenAI(api_key="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")

FILE_PATH = "records.txt"

st.title("학생 지도 멘트 생성")

def load_records():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.readlines()[::-1]

records = load_records()

if records:
    selected = st.selectbox("기록 선택", records)

    if st.button("멘트 생성"):
        prompt = f"""
        다음은 초등학교에서 발생한 생활지도 상황이다.

        상황:
        {selected}

        위 상황을 바탕으로:
        1. 학생에게 할 지도 멘트 (부드러운 버전)
        2. 학생에게 할 지도 멘트 (단호한 버전)

        초등학생 수준에 맞게, 교육적으로 작성하라.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write(response.choices[0].message.content)

else:
    st.write("저장된 기록이 없습니다.")