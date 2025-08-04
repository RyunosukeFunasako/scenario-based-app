import streamlit as st
import time

if st.session_state.current_page == "rapport":
    with st.sidebar:
        st.markdown(f"### 実験の進度")
        st.progress(4 / 5)

    # rapportアンケート画面
    st.title("カウンセラーとしての評価")
    st.write("カウンセラーエージェントとの「信頼関係」を測る質問に回答していただきます。  \n1を「全くそう思わない」、5を「全くそう思う」として、1~5点で評価してください。")
    
    questions = {
        "**Q1: カウンセラーエージェントは私を理解した**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q2: カウンセラーエージェントは意欲的に見えなかった**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q3: カウンセラーエージェントはワクワクしていた**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q4: カウンセラーエージェントの動きは自然ではなかった**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q5: カウンセラーエージェントはフレンドリーだった**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q6: カウンセラーエージェントは私に注意を払っていなかった**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q7: カウンセラーエージェントと私は共通の目標に向かって行動した**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q8: カウンセラーエージェントと私の心は通っていないようだった**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q9: カウンセラーエージェントとの身体的なつながりを感じた**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q10: カウンセラーエージェントが私を信頼していると感じた**": [
            1,
            2,
            3,
            4,
            5
        ],
        "**Q11: カウンセラーエージェントのことが理解できなかった**": [
            1,
            2,
            3,
            4,
            5
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
            st.session_state.rapport_answers = scores
            st.success("回答ありがとうございました。")
            time.sleep(1)
            st.session_state.current_page = "quality"
            st.rerun()

else:
    st.session_state.current_page = "description"
    st.rerun()
