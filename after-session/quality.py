import streamlit as st
import time

if st.session_state.current_page == "quality":
    with st.sidebar:
        st.markdown(f"### 実験の進度")
        st.progress(5 / 5)

    # qualityアンケート画面
    st.title("対話システムとしての評価")
    st.write("カウンセラーエージェントの「対話の質」を測る質問に回答していただきます。  \n0を「全くそう思わない」、10を「全くそう思う」として、0~10点で評価してください。")
    
    questions = {
        "**Q1: カウンセラーエージェントの発話は人間らしく自然だった**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q2: 簡単に対話を続けることができた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q3: カウンセラーエージェントとの対話は楽しかった**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q4: カウンセラーエージェントの発話に共感できた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q5: カウンセラーエージェントはあなたに興味を持って積極的に話そうとしていた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q6: カウンセラーエージェントの話したことは信頼できると感じた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q7: カウンセラーエージェントの個性・人となりが感じられた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q8: カウンセラーエージェントは自身の考えをもって話していると感じた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q9: カウンセラーエージェントには話したい話題があると感じた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q10: カウンセラーエージェントは感情を持っていると感じた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q11: カウンセラーエージェントの発話は矛盾せず一貫していた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q12: この対話にのめりこめた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q13: またこのカウンセラーエージェントと話したい**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q14: カウンセラーエージェントは共感を示した**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ],
        "**Q15: カウンセラーエージェントは対話の主導権を握ることができた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10
        ]
    }
    scores = {}
    unanswered = []
    for q_label, options in questions.items():
        answer = st.radio(q_label, options, index=None, key=q_label, horizontal=True)
        if answer is not None:
            scores[q_label] = answer
        else:
            unanswered.append(q_label)
    if st.button("回答を提出"):
        if unanswered:
            st.warning("以下の質問にまだ回答していません：")
            for q in unanswered:
                st.markdown(f"- {q}")
        else:
            st.session_state.quality_answers = scores
            st.success("回答ありがとうございました。")
            time.sleep(1)
            st.session_state.current_page = "thanks"
            st.rerun()

else:
    st.session_state.current_page = "description"
    st.rerun()
