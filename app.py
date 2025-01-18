import streamlit as st

# 캐릭터 매칭 기준
character_map = {
    "ENFP": "피카츄 - 열정적인 모험가",
    "ESTP": "지우 - 에너지 넘치는 리더",
    "ISTJ": "이슬이 - 논리적 전략가",
    "ISFJ": "웅 - 자상한 지원자",
    "ENTP": "로켓단 - 창의적인 아이디어 제조기",
}

# 질문 및 답변
questions = [
    ("새로운 환경에서 당신은?", ["적극적으로 나선다 (E)", "천천히 적응한다 (I)"]),
    ("계획을 세울 때 당신은?", ["꼼꼼히 준비한다 (J)", "유연하게 움직인다 (P)"]),
    # ... 위에서 작성한 20개의 질문을 여기에 추가 ...
]

# Streamlit 앱 시작
st.title("포켓몬 성향 테스트")
st.write("아래 질문에 답해 당신의 성향을 확인하세요!")

# 사용자 입력 저장
answers = []
for i, (question, options) in enumerate(questions):
    st.write(f"**{i+1}. {question}**")
    choice = st.radio("", options, key=i)
    answers.append(choice.split(" ")[-1])  # MBTI 코드만 저장

# 결과 계산
if st.button("결과 보기"):
    mbti = ""
    mbti += "E" if answers.count("E") > answers.count("I") else "I"
    mbti += "N" if answers.count("N") > answers.count("S") else "S"
    mbti += "F" if answers.count("F") > answers.count("T") else "T"
    mbti += "J" if answers.count("J") > answers.count("P") else "P"
    
    character = character_map.get(mbti, "알 수 없는 캐릭터")
    st.subheader(f"당신의 성향은: {character}!")
    st.write(f"MBTI 결과: {mbti}")
