import streamlit as st

# 질문과 선택지, 각 선택지가 가지는 점수(가중치)를 정의합니다.
# scores 딕셔너리는 { "adventure": 점수, "sociability": 점수, "logic": 점수, "kindness": 점수 } 형태로 구성
QUESTIONS = [
    {
        "question": "1) 친구들과 주말 계획을 세울 때, 당신은?",
        "answers": [
            {"text": "다양한 곳을 여행하고 싶다고 제안한다", "scores": {"adventure": 2}},
            {"text": "가까운 곳에서 편하게 놀자고 제안한다", "scores": {"sociability": 2}},
            {"text": "일정을 꼼꼼히 계획하고 조율한다", "scores": {"logic": 2}},
            {"text": "친구가 원하는 대로 맞춰준다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "2) 새로운 일을 맡았을 때, 당신은?",
        "answers": [
            {"text": "일단 직접 부딪히며 시도해본다", "scores": {"adventure": 2}},
            {"text": "동료들과 함께 의논하며 해결한다", "scores": {"sociability": 2}},
            {"text": "먼저 매뉴얼이나 자료부터 찾아본다", "scores": {"logic": 2}},
            {"text": "주변에서 도움이 필요한 사람부터 챙긴다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "3) 모처럼 휴가가 생겼다면, 당신의 선택은?",
        "answers": [
            {"text": "해외여행이나 액티비티를 찾는다", "scores": {"adventure": 2}},
            {"text": "친구들과 만나 파티나 모임을 가진다", "scores": {"sociability": 2}},
            {"text": "집에서 책이나 영화로 지식을 쌓는다", "scores": {"logic": 2}},
            {"text": "가족이나 지인을 먼저 챙기는 시간을 갖는다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "4) 대화를 할 때, 당신의 스타일은?",
        "answers": [
            {"text": "이야기를 유쾌하게 이끌어 가는 편이다", "scores": {"adventure": 1, "sociability": 1}},
            {"text": "상대방에게 질문을 많이 하며 친해지려 한다", "scores": {"sociability": 2}},
            {"text": "논리적으로 상황을 분석해가며 대화한다", "scores": {"logic": 2}},
            {"text": "상대방의 감정을 살피며 공감하는 편이다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "5) 게임을 할 때, 당신은 주로 어떤 역할을 선호하나요?",
        "answers": [
            {"text": "탱커나 전사처럼 앞장서서 싸운다", "scores": {"adventure": 2}},
            {"text": "파티 플레이에서 친구들과 합을 맞추는 것이 좋다", "scores": {"sociability": 2}},
            {"text": "전략을 세우고 지휘하는 리더 역할을 맡는다", "scores": {"logic": 2}},
            {"text": "힐러나 버퍼처럼 팀원을 지원하는 역할을 맡는다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "6) 친구가 고민을 상담해 올 때, 당신은?",
        "answers": [
            {"text": "바로 직접적인 해결책을 시도해보자고 권한다", "scores": {"adventure": 2}},
            {"text": "함께 만나서 이야기를 많이 들어준다", "scores": {"sociability": 2}},
            {"text": "문제의 원인과 해결 방안을 분석적으로 제시한다", "scores": {"logic": 2}},
            {"text": "정서적으로 공감해주고 위로에 집중한다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "7) 새로운 취미를 갖게 된다면, 어떤 것을 가장 먼저 해보고 싶나요?",
        "answers": [
            {"text": "번지점프, 스카이다이빙 같은 극한 스포츠", "scores": {"adventure": 2}},
            {"text": "합창단, 댄스동호회 등 사람들과 함께 하는 활동", "scores": {"sociability": 2}},
            {"text": "퍼즐, 보드게임, 프로그래밍 등 머리를 쓰는 활동", "scores": {"logic": 2}},
            {"text": "봉사활동, 반려동물 돌보기 등 타인과 함께하는 나눔활동", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "8) 당신은 약속 시간에 대해 어떻게 생각하나요?",
        "answers": [
            {"text": "살짝 늦어도 괜찮으니 현장 분위기에 맞춘다", "scores": {"adventure": 1}},
            {"text": "친구와 대화하면서 유동적으로 변경해도 괜찮다", "scores": {"sociability": 1}},
            {"text": "정확한 시간에 맞춰서 움직이는 편이다", "scores": {"logic": 2}},
            {"text": "상대방이 불편하지 않도록 미리 일찍 도착한다", "scores": {"kindness": 1, "logic": 1}},
        ],
    },
    {
        "question": "9) 대규모 파티에 초대받았을 때, 당신의 반응은?",
        "answers": [
            {"text": "새로운 사람들과 어울리는 것에 설렌다", "scores": {"adventure": 1, "sociability": 1}},
            {"text": "아는 사람들에게 먼저 연락해 함께 가길 권유한다", "scores": {"sociability": 2}},
            {"text": "파티 분위기, 드레스 코드 등 정보를 먼저 찾는다", "scores": {"logic": 2}},
            {"text": "모임에서 소외되는 사람이 없도록 챙긴다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "10) 문제를 해결해야 할 때 가장 먼저 하는 행동은?",
        "answers": [
            {"text": "바로 실행해보면서 배우는 편이다", "scores": {"adventure": 2}},
            {"text": "함께 해결할 사람을 찾거나 팀을 꾸린다", "scores": {"sociability": 2}},
            {"text": "철저히 계획하고 자료 조사를 먼저 한다", "scores": {"logic": 2}},
            {"text": "주변에서 도움 필요한 사람을 살피면서 같이 해결한다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "11) 휴일에 갑자기 혼자만의 시간이 생긴다면?",
        "answers": [
            {"text": "바로 카메라 챙겨서 가까운 곳이라도 나가본다", "scores": {"adventure": 2}},
            {"text": "지인에게 연락해 함께 놀 계획을 잡는다", "scores": {"sociability": 2}},
            {"text": "집에서 공부나 자기계발을 한다", "scores": {"logic": 2}},
            {"text": "부모님이나 가족에게 전화나 문자를 먼저 보낸다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "12) 동아리나 학회, 스터디 모임에서의 당신은?",
        "answers": [
            {"text": "새로운 프로젝트나 활동을 제안한다", "scores": {"adventure": 2}},
            {"text": "사람들과 친목 도모에 힘쓴다", "scores": {"sociability": 2}},
            {"text": "정보를 수집하고 효율적으로 진행할 방법을 제시한다", "scores": {"logic": 2}},
            {"text": "팀원들이 어려움 없이 참여하도록 돕는다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "13) 스트레스를 풀기 위해 가장 하고 싶은 일은?",
        "answers": [
            {"text": "스포츠나 액티비티로 땀 흘리고 풀기", "scores": {"adventure": 2}},
            {"text": "친구와 수다 떨고 노래방 가기", "scores": {"sociability": 2}},
            {"text": "책을 읽거나 새로운 지식을 찾아보기", "scores": {"logic": 2}},
            {"text": "봉사활동, 기부 등 마음이 따뜻해지는 일 하기", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "14) 낯선 사람과 대화를 시작해야 할 때, 당신은?",
        "answers": [
            {"text": "가벼운 농담이나 에피소드로 분위기를 푼다", "scores": {"adventure": 1, "sociability": 1}},
            {"text": "상대에게 질문을 던지며 관심사를 찾는다", "scores": {"sociability": 2}},
            {"text": "목적이나 상황에 대해 먼저 파악하고 핵심을 묻는다", "scores": {"logic": 2}},
            {"text": "상대방이 불편해하지 않도록 미소와 배려를 먼저 보인다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "15) 여행 계획을 짤 때, 당신의 우선순위는?",
        "answers": [
            {"text": "모험 가득한 스팟이나 액티비티 찾기", "scores": {"adventure": 2}},
            {"text": "친구들과 즐길 수 있는 코스 위주로 선정", "scores": {"sociability": 2}},
            {"text": "이동 동선과 예산 등을 꼼꼼히 계산", "scores": {"logic": 2}},
            {"text": "함께 가는 사람들이 편안하고 즐겁게 지낼 수 있는 곳", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "16) 팀 프로젝트에서 당신이 주로 맡는 역할은?",
        "answers": [
            {"text": "새로운 아이디어를 내고 실행하는 추진자", "scores": {"adventure": 2}},
            {"text": "팀원 간의 소통과 협력을 이끄는 분위기 메이커", "scores": {"sociability": 2}},
            {"text": "자료 조사와 분석, 계획을 세우는 브레인", "scores": {"logic": 2}},
            {"text": "필요한 곳에 도움을 주고 갈등을 조정하는 서포터", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "17) 새로운 기술이나 지식을 배울 때, 당신은?",
        "answers": [
            {"text": "직접 해보면서 시행착오를 겪어가며 배운다", "scores": {"adventure": 2}},
            {"text": "사람들과 함께 프로젝트나 스터디를 꾸려서 배운다", "scores": {"sociability": 2}},
            {"text": "책, 온라인 강의, 자료 등을 보며 체계적으로 학습한다", "scores": {"logic": 2}},
            {"text": "함께 배우는 사람들의 진도를 챙겨주고 격려한다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "18) 친구가 깜짝 파티를 열자고 제안했다면, 당신은?",
        "answers": [
            {"text": "바로 장소와 이벤트 아이디어를 몇 가지 찾는다", "scores": {"adventure": 2}},
            {"text": "함께 파티에 올 사람들에게 연락해서 참여를 유도한다", "scores": {"sociability": 2}},
            {"text": "예산과 일정, 필요한 물품 리스트를 만들어본다", "scores": {"logic": 2}},
            {"text": "주변에서 도움이 필요한 파트가 있는지 먼저 묻는다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "19) 막다른 상황에서 벗어날 방법을 찾으려 할 때, 당신은?",
        "answers": [
            {"text": "확실한 돌파구가 떠오를 때까지 여러 시도를 해본다", "scores": {"adventure": 2}},
            {"text": "조언을 구할 만한 사람들을 리스트업하고 의견을 듣는다", "scores": {"sociability": 2}},
            {"text": "문제의 근본 원인과 해결책을 분석적으로 정리한다", "scores": {"logic": 2}},
            {"text": "같이 고민 중인 사람들에게 격려와 응원을 아끼지 않는다", "scores": {"kindness": 2}},
        ],
    },
    {
        "question": "20) 당신의 인생 가치관에 가장 가까운 문장은?",
        "answers": [
            {"text": "인생은 도전! 실패해도 시도 자체가 의미 있다", "scores": {"adventure": 2}},
            {"text": "함께하면 무엇이든 해낼 수 있다", "scores": {"sociability": 2}},
            {"text": "아는 것이 힘이다. 제대로 이해하고 움직여라", "scores": {"logic": 2}},
            {"text": "서로 도우며 함께 행복해지는 길을 찾자", "scores": {"kindness": 2}},
        ],
    },
]

# 성향 점수에 따라 결과를 매핑할 포켓몬 정보를 정의합니다.
# 가장 높은 점수가 나온 성향이 어떤 포켓몬과 연결될지 간단히 예시를 만듭니다.
POKEMON_RESULTS = {
    "adventure": {
        "name": "파이리",
        "description": "모험심이 넘치는 당신은 불타입 파이리! 뜨거운 열정과 도전 정신으로 주변을 활기차게 만들어요.",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
    },
    "sociability": {
        "name": "피카츄",
        "description": "사교성이 뛰어난 당신은 전기타입 피카츄! 친구들과의 어울림을 좋아하고 모든 이들에게 사랑받는 성격이에요.",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    },
    "logic": {
        "name": "이상해씨",
        "description": "논리적이고 분석적인 당신은 풀타입 이상해씨! 차분하고 똑똑한 면모로 주변 문제를 해결해요.",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
    },
    "kindness": {
        "name": "꼬부기",
        "description": "배려심이 많은 당신은 물타입 꼬부기! 포근한 마음으로 모두를 편안하게 해주는 사랑스러운 존재예요.",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
    },
}


def main():
    st.title("포켓몬 성향 테스트")
    st.write("20개의 질문에 답변하시면, 당신의 성향에 어울리는 포켓몬을 찾아드립니다!")

    # 사용자 성향 점수를 저장할 딕셔너리(초기값 0)
    if "scores" not in st.session_state:
        st.session_state.scores = {
            "adventure": 0,
            "sociability": 0,
            "logic": 0,
            "kindness": 0,
        }

    # 사용자가 질문에 답했는지 확인하기 위해 session_state에 답변 기록
    if "answers" not in st.session_state:
        st.session_state.answers = [None] * len(QUESTIONS)

    # 각 질문에 대해 Radio 버튼을 이용해 선택지를 표시
    for i, q in enumerate(QUESTIONS):
        st.write("")
        st.subheader(q["question"])

        # 이미 선택한 답변이 있다면 해당 값으로 설정
        current_answer = st.session_state.answers[i]

        # Radio로 사용자 선택을 받고, 변경 시 scores를 업데이트
        choice = st.radio(
            label="",
            options=[ans["text"] for ans in q["answers"]],
            index=current_answer if current_answer is not None else 0,
            key=f"question_{i}",
        )

        # 사용자가 선택을 변경할 때마다 점수 다시 계산
        # 전체 질문에 대해 매번 재계산(간단구현) or 마지막에만 계산하는 방식 등 다양하게 가능
        # 여기서는 간단 구현을 위해 선택할 때마다 전체 scores 초기화 후 다시 누적
        st.session_state.answers[i] = [ans["text"] for ans in q["answers"]].index(choice)
        
        # 매 질문마다 초기화 후 다시 계산하기 위해 일단 0으로 초기화
        st.session_state.scores = {
            "adventure": 0,
            "sociability": 0,
            "logic": 0,
            "kindness": 0,
        }
        # 모든 질문의 선택지 점수를 합산
        for j, qq in enumerate(QUESTIONS):
            ans_index = st.session_state.answers[j]
            if ans_index is not None:
                # qq["answers"][ans_index]["scores"] 를 읽어서 st.session_state.scores에 더함
                for key, val in qq["answers"][ans_index]["scores"].items():
                    st.session_state.scores[key] += val

    st.write("---")

    # 모든 질문에 답변한 후 "결과 보기" 버튼
    if st.button("결과 보기"):
        # 현재까지 누적된 성향 점수를 가져옴
        final_scores = st.session_state.scores
        # 가장 높은 점수를 받은 성향 찾기
        best_trait = max(final_scores, key=final_scores.get)
        pokemon_info = POKEMON_RESULTS[best_trait]

        st.success(f"당신에게 어울리는 포켓몬은 바로 **{pokemon_info['name']}**!")
        st.write(pokemon_info["description"])
        if pokemon_info["image_url"]:
            st.image(pokemon_info["image_url"], width=150)


if __name__ == "__main__":
    main()
