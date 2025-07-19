import streamlit as st
import json
from datetime import datetime

st.title("実験終了！！！")
st.markdown("""
お疲れ様でした！！！
実験は以上となります。

最後に、以下の「実験の結果をダウンロード」ボタンを押下してください。  
ダウンロードしたファイルはGoogleフォームに添付してください。 
            
実験へのご協力ありがとうございました！！！
""")

result_data = {
    "qids": st.session_state.get("qids_answers", {}),
    "dialogue_history": st.session_state.get("dialogue_history", []),
    "deviation_history": st.session_state.get("deviation_history", []),
    "cc_immediate": st.session_state.get("cc_immediate_answers", {}),
    "rapport": st.session_state.get("rapport_answers", {}),
    "quality": st.session_state.get("quality_answers", {}),
}

result_json = json.dumps(result_data, ensure_ascii=False, indent=2)
now = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"experiment_result_{now}.json"

st.download_button(
    label="実験の結果をダウンロード",
    data=result_json,
    file_name=file_name,
    mime="application/json"
)