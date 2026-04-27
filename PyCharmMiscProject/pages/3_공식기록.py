import streamlit as st
import os

FILE_PATH = "records.txt"

st.title("공식 기록 문장 생성")


def load_records():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.readlines()[::-1]


records = load_records()

if records:
    selected = st.selectbox("기록 선택", records)

    if st.button("기록 문장 생성"):
        result = f"""
        학생 간의 상호작용 과정에서 갈등 상황이 발생하였으며,
        이에 대해 교사의 지도 하에 서로의 입장을 이해하고 문제를 해결하도록 지도함.

        (사건 내용: {selected})
        """

        st.subheader("공식 기록 문장")
        st.write(result)

else:
    st.write("저장된 기록이 없습니다.")