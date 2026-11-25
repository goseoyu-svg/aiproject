
import streamlit as st
import random

# --------------------------------
# 페이지 설정
# --------------------------------
st.set_page_config(
    page_title="혈액형별 진로 탐험 🚀",
    page_icon="🩸",
    layout="centered"
)

# --------------------------------
# 디자인
# --------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5, #e6f4ff);
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #6C63FF;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #555555;
}

.job-card {
    background-color: white;
    padding: 22px;
    border-radius: 18px;
    border: 2px solid #e0d7ff;
    margin-bottom: 15px;
}

.job-title {
    font-size: 24px;
    font-weight: bold;
    color: #6C63FF;
}

.info {
    font-size: 16px;
    line-height: 1.8;
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------
# 제목
# --------------------------------
st.markdown(
    '<div class="main-title">🩸 혈액형별 진로 탐험 🚀</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    '나에게 어울리는 미래의 직업은 무엇일까? 🔍'
    '</div>',
    unsafe_allow_html=True
)

st.write("")
st.info(
    "💡 혈액형은 재미있는 진로 탐색의 출발점이야! "
    "실제 진로는 자신의 흥미와 적성에 따라 자유롭게 선택하면 돼."
)

# --------------------------------
# 진로 데이터
# --------------------------------
career_data = {
    "A형": [
        {
            "job": "🎨 UX/UI 디자이너",
            "major": "시각디자인학과, 산업디자인학과, "
                     "디지털미디어디자인학과",
            "personality": "꼼꼼하게 관찰하고 세심하게 "
                           "디자인하는 것을 좋아하는 사람",
            "description": "사람들이 편리하게 사용할 수 있도록 "
                           "앱이나 웹사이트의 화면과 기능을 디자인해.",
            "strength": "창의력, 관찰력, 꼼꼼함"
        },
        {
            "job": "🔬 생명과학 연구원",
            "major": "생명과학과, 생명공학과, 생화학과",
            "personality": "호기심이 많고 작은 변화도 "
                           "놓치지 않는 사람",
            "description": "생명체의 원리를 연구하고 새로운 "
                           "기술과 의학 발전에 기여하는 직업이야.",
            "strength": "탐구력, 집중력, 분석력"
        }
    ],

    "B형": [
        {
            "job": "🎬 콘텐츠 크리에이터",
            "major": "미디어커뮤니케이션학과, 영상학과, "
                     "광고홍보학과",
            "personality": "새로운 아이디어를 떠올리고 "
                           "자신만의 방식으로 표현하는 사람",
            "description": "영상, 사진, 글 등 다양한 콘텐츠를 "
                           "기획하고 제작하는 직업이야.",
            "strength": "창의력, 표현력, 도전 정신"
        },
        {
            "job": "🎮 게임 기획자",
            "major": "게임학과, 컴퓨터공학과, "
                     "디지털콘텐츠학과",
            "personality": "상상력이 풍부하고 새로운 "
                           "놀이와 이야기를 만드는 것을 좋아하는 사람",
            "description": "게임의 스토리와 규칙, 캐릭터, "
                           "시스템 등을 기획하는 직업이야.",
            "strength": "상상력, 기획력, 문제 해결 능력"
        }
    ],

    "O형": [
        {
            "job": "⚽ 스포츠 지도자",
            "major": "체육학과, 스포츠과학과, "
                     "스포츠지도학과",
            "personality": "사람들과 함께 활동하고 "
                           "목표를 향해 도전하는 것을 좋아하는 사람",
            "description": "운동 기술을 가르치고 선수나 "
                           "일반인의 건강과 체력 향상을 도와줘.",
            "strength": "리더십, 소통 능력, 도전 정신"
        },
        {
            "job": "🏢 창업가",
            "major": "경영학과, 경제학과, "
                     "창업학과, 산업공학과",
            "personality": "새로운 기회를 찾고 자신의 "
                           "아이디어를 직접 실현하고 싶은 사람",
            "description": "새로운 사업을 기획하고 운영하며 "
                           "사람들에게 가치 있는 서비스를 만들어.",
            "strength": "추진력, 도전 정신, 의사소통 능력"
        }
    ],

    "AB형": [
        {
            "job": "🤖 인공지능 개발자",
            "major": "컴퓨터공학과, 인공지능학과, "
                     "소프트웨어학과",
            "personality": "논리적으로 생각하고 새로운 "
                           "기술을 배우는 것을 즐기는 사람",
            "description": "인공지능 프로그램과 서비스를 "
                           "개발하고 다양한 문제를 해결해.",
            "strength": "논리력, 분석력, 학습 능력"
        },
        {
            "job": "🌍 국제기구 전문가",
            "major": "국제학과, 정치외교학과, "
                     "국제개발협력학과, 행정학과",
            "personality": "다양한 문화에 관심이 많고 "
                           "사회 문제를 해결하는 데 관심이 있는 사람",
            "description": "국제기구나 관련 기관에서 "
                           "국가 간 협력과 글로벌 문제 해결에 참여해.",
            "strength": "의사소통 능력, 공감 능력, 분석력"
        }
    ]
}

# --------------------------------
# 혈액형 선택
# --------------------------------
st.markdown("### 🩸 나의 혈액형을 선택해 봐!")

blood_type = st.selectbox(
    "어떤 혈액형인가요?",
    ["선택하세요", "A형", "B형", "O형", "AB형"]
)

# --------------------------------
# 진로 추천 결과
# --------------------------------
if blood_type != "선택하세요":

    st.markdown("---")

    st.markdown(
        f"## 🎉 {blood_type}을(를) 선택했구나!"
    )

    st.write(
        "지금부터 두 가지 진로를 소개할게. "
        "마음에 드는 직업을 찾아보자! 💕"
    )

    careers = career_data[blood_type]

    for i, career in enumerate(careers, 1):

        st.markdown(
            f"""
            <div class="job-card">
                <div class="job-title">
                    {i}. {career['job']}
                </div>
                <div class="info">
                    <b>📖 추천 학과</b><br>
                    {career['major']}<br><br>

                    <b>💖 어울리는 성격</b><br>
                    {career['personality']}<br><br>

                    <b>💼 어떤 일을 할까?</b><br>
                    {career['description']}<br><br>

                    <b>🌟 필요한 역량</b><br>
                    {career['strength']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # 마무리 메시지
    # --------------------------------
    st.success(
        "✨ 두 가지 직업 중 어떤 것이 가장 마음에 들었어?"
    )

    st.markdown("### 💬 나만의 진로 생각해 보기")

    favorite = st.radio(
        "더 관심이 가는 진로를 골라 봐!",
        [careers[0]["job"], careers[1]["job"], "아직 잘 모르겠어 🤔"]
    )

    if st.button("나의 선택 확인하기 🎯"):

        st.balloons()

        if favorite == "아직 잘 모르겠어 🤔":
            st.info(
                "괜찮아! 진로는 천천히 찾아가도 돼. "
                "다양한 경험을 하면서 나만의 꿈을 발견해 보자! 🌱"
            )
        else:
            st.success(
                f"👏 멋진 선택이야! {favorite}에 대해 "
                "조금 더 알아보면 좋겠어!"
            )

# --------------------------------
# 하단 안내
# --------------------------------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#777;">
        🌈 나의 가능성은 혈액형보다 훨씬 다양해!<br>
        나만의 꿈을 향해 한 걸음씩 나아가 보자! 🚀
    </div>
    """,
    unsafe_allow_html=True
)
