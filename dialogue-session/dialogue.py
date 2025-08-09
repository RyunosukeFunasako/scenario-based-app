import streamlit as st
from openai import OpenAI
import json
import time

# ストリーム表示を行う関数
def stream_counselor_reply(counselor_reply):
    for chunk in counselor_reply:
        yield chunk
        time.sleep(0.02)

# 対話セッション
if st.session_state.current_page == "dialogue":
    st.title("対話セッション")

    scenario_file = "dialogue-session/counselor_scenario.json"

    if "counselor_turn" not in st.session_state:
        st.session_state.counselor_turn = 0

    if "messages_for_counselor" not in st.session_state:
        st.session_state.messages_for_counselor = []

    with open(scenario_file, "r") as f:
        scenario_data = json.load(f)["counselor_scenario"]

    # サイドバーにターン進捗を表示
    with st.sidebar:
        st.markdown(f"### 実験の進度")
        st.progress(2 / 5)
        st.markdown(f"### 対話セッションの進度")
        st.progress((st.session_state.counselor_turn + 1) / len(scenario_data))
        st.markdown(f"**{st.session_state.counselor_turn + 1} / {len(scenario_data)} ターン**")
    
    # 対話履歴を表示し続ける
    for dialogue_history in st.session_state.dialogue_history:
        with st.chat_message(dialogue_history["role"]):
            st.markdown(dialogue_history["content"])
    
    # 現在のターンのカウンセラーエージェントの発話を生成・表示
    if st.session_state.counselor_turn < len(scenario_data):
        # まだ表示されていない発話のみをストリーミング表示する
        if len(st.session_state.messages_for_counselor) == st.session_state.counselor_turn:
            counselor_scenario_message = scenario_data[st.session_state.counselor_turn]["counselor_message"]
            # 表示を遅らせる
            time.sleep(2)
            counselor_reply = counselor_scenario_message
                
            # カウンセラーエージェントの発話をストリーム表示
            with st.chat_message("assistant"):
                st.write_stream(stream_counselor_reply(counselor_reply))

            # 対話履歴に追加
            st.session_state.dialogue_history.append({"role": "assistant", "content": counselor_reply})
            st.session_state.messages_for_counselor.append({"role": "assistant", "content": counselor_reply})
    
    # 被験者の入力（23ターン目は入力を求めない）
    if st.session_state.counselor_turn < len(scenario_data) - 1:
        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_input("あなたの返答を入力してください", key="chat_input")
            submitted = st.form_submit_button("送信")

        if submitted and user_input:
            st.session_state.dialogue_history.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)
            st.session_state.counselor_turn += 1
            st.rerun()
    
    # 23ターン終了
    else:
        time.sleep(1)
        st.success("これで対話セッションは終了です。")
        if st.button("「認知の変化の回答」に進む"):
            st.session_state.current_page = "cc_immediate"
            st.rerun()

else:
    st.session_state.current_page = "description"
    st.rerun()