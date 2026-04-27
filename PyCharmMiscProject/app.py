import streamlit as st
import os

FILE_PATH = "records.txt"

st.title("생활지도 기록 시스템")

# --------------------------
# 1. 사건 기본 정보 (날짜 + 시간 직접 입력)
# --------------------------
st.subheader("사건 기본 정보")

date = st.date_input("날짜 선택")

# 시간 직접 입력
time = st.text_input("시간 입력 (예: 10:30)")

date_time = f"{date} {time}"

place = st.text_input("장소")

# --------------------------
# 2. 관련 학생 (동적 추가)
# --------------------------
st.subheader("관련 학생")

if "students" not in st.session_state:
    st.session_state.students = [""]

for i in range(len(st.session_state.students)):
    st.session_state.students[i] = st.text_input(
        f"학생 {i + 1}",
        st.session_state.students[i],
        key=f"student_{i}"
    )

if st.button("학생 추가"):
    st.session_state.students.append("")

# --------------------------
# 3. 사건 유형
# --------------------------
st.subheader("사건 유형")

incident_type = st.radio(
    "",
    ["말다툼", "신체적 충돌", "따돌림", "규칙 위반", "기타"]
)

custom_type = ""
if incident_type == "기타":
    custom_type = st.text_input("기타 유형 입력")

# --------------------------
# 4. 사건 경위
# --------------------------
st.subheader("사건 경위")

description = st.text_area("내용 입력", height=150)


# --------------------------
# 저장 / 불러오기 함수
# --------------------------

def save_record(data):
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(data + "\n")


def load_records():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.readlines()[::-1]


def delete_record(index):
    if not os.path.exists(FILE_PATH):
        return

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines.pop(len(lines) - 1 - index)

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)


# --------------------------
# 저장 버튼
# --------------------------

if st.button("기록 추가하기"):

    students_list = [s for s in st.session_state.students if s.strip() != ""]
    students = ", ".join(students_list)

    if not place or not students or not description or not time:
        st.error("반드시 입력해야 합니다.")
    else:
        final_type = custom_type if incident_type == "기타" else incident_type

        record = f"{date_time} / {place} | {students} | {final_type} | {description}"

        save_record(record)
        st.success("저장되었습니다.")

        st.session_state.students = [""]

# --------------------------
# 기록 출력
# --------------------------

st.subheader("최근 생활지도 기록")

records = load_records()

if records:
    for i, r in enumerate(records):

        if "말다툼" in r:
            st.markdown(f"<span style='color:orange'>{r}</span>", unsafe_allow_html=True)
        elif "신체적 충돌" in r:
            st.markdown(f"<span style='color:red'>{r}</span>", unsafe_allow_html=True)
        elif "따돌림" in r:
            st.markdown(f"<span style='color:purple'>{r}</span>", unsafe_allow_html=True)
        elif "규칙 위반" in r:
            st.markdown(f"<span style='color:blue'>{r}</span>", unsafe_allow_html=True)
        else:
            st.write(r)

        if st.button("삭제", key=f"delete_{i}"):
            delete_record(i)
            st.experimental_rerun()

else:
    st.write("저장된 기록이 없습니다.")
