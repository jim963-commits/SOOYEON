import streamlit as st
import os

FILE_PATH = "records.txt"

st.title("학부모 상담 문장 생성")


def load_records():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.readlines()[::-1]


records = load_records()

if records:
    selected = st.selectbox("기록 선택", records)

    if st.button("상담 문장 생성"):
        result = f"""
        안녕하세요, 학부모님.

        오늘 학교에서 {selected}와 관련된 상황이 있었습니다.

        학생들이 서로의 입장을 이해하고 바람직한 방향으로 행동할 수 있도록 지도하였습니다.
        가정에서도 대화를 통해 올바른 행동에 대해 지도해 주시면 감사하겠습니다.

        감사합니다.
        """

        st.subheader("학부모 상담 문장")
        st.write(result)

else:
    st.write("저장된 기록이 없습니다.")