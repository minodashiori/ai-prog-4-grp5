import streamlit as st
import os
from groq import Groq

# 環境変数から API キーを取得
api_key = "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"
if not api_key:
    st.error("APIキーが設定されていません。")
    st.stop()

# Groq クライアントの初期化
client = Groq(api_key=api_key)

def get_response(question):
    """ Groq API を使用してチャット応答を取得する関数 """
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": question}
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title('Groq API デモ')

# ユーザー入力
user_input = st.text_input("質問を入力してください:")

if st.button('回答を取得'):
    with st.spinner('回答を取得中...'):
        response = get_response(user_input)
        st.write(response)