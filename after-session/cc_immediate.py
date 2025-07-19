import streamlit as st
import time

if st.session_state.current_page == "cc_immediate":
    with st.sidebar:
        st.markdown(f"### 実験の進度")
        st.progress(3 / 5)

    # CC-immediateアンケート画面
    st.title("認知の変化の回答")
    st.write("認知の即時的変化を測る質問（CC-immediate）に回答していただきます。  \n対話セッションに対してどのように感じたか、次の尺度を使ってお答えください。")
    st.markdown("""
**評価尺度の説明：**

| 選択肢 | 意味 |
|------|------|
| 0    | 全くそう思わない |
| 1    |  |
| 2    | ややそう思う |
| 3    |  |
| 4    | かなりそう思う |
| 5    |  |
| 6    | 全くそう思う |
""")
    
    questions = {
        "**Q1: このセッションの中で、否定的に考えることが少なくなっていることに気づいた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6
        ],
        "**Q2: このセッションの中で、否定的な考えに気づき、それが偏っていることを認識し、状況を再評価した**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6
        ],
        "**Q3: このセッションの中で、長い間抱えていた否定的な信念が正しくないかもしれないと気づいた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6
        ],
        "**Q4: このセッションの中で、自分が考えていることに注目し、よりバランスの取れた見方をするよう努めた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6
        ],
        "**Q5: このセッションの中で、否定的な考えが正確ではないかもしれないと考えた**": [
            0,
            1,
            2,
            3,
            4,
            5,
            6
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
            st.session_state.cc_immediate_answers = scores
            st.success("回答ありがとうございました。")
            time.sleep(1)
            st.session_state.current_page = "rapport"
            st.rerun()

else:
    st.session_state.current_page = "description"
    st.rerun()
