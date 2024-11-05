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

# ストーリーの概要を生成する関数
def generate_story_outline(genre, protagonist, length):
    story_outline = ""
    if genre == "ファンタジー":
        story_outline += f"ある日、{protagonist}は魔法の王国で冒険を始めました。"
    elif genre == "SF":
        story_outline += f"未来の世界で、{protagonist}は宇宙船に乗り込んで未知の惑星を目指しました。"
    elif genre == "ミステリー":
        story_outline += f"{protagonist}は小さな町で発生した奇妙な事件を調査し始めました。"
    else:
        story_outline += f"{protagonist}の物語が始まりました。"

    if length == "短編":
        story_outline += f" 短い冒険で、{protagonist}はすぐに目的地に到着し、心に残る体験をしました。"
    elif length == "中編":
        story_outline += f" {protagonist}は数々の困難に立ち向かい、成長していきました。やがて、一つの大きな試練に挑みました。"
    elif length == "長編":
        story_outline += f" 長い旅路を通して、{protagonist}は多くの仲間と出会い、ついに運命的な敵と対決することになりました。"

    return story_outline

# Groq APIを使用してストーリーの詳細を生成
def get_story_from_groq(outline):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": outline}
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title('ストーリー生成アプリ with Groq API')

# ジャンル、主人公、ストーリーの長さを選択するためのインターフェース
genre = st.selectbox("ストーリーのジャンルを選んでください", ["ファンタジー", "SF", "ミステリー", "その他"])
protagonist = st.text_input("主人公の設定を入力してください（例: 勇敢な騎士、天才科学者など）")
length = st.selectbox("ストーリーの長さを選んでください", ["短編", "中編", "長編"])

# ボタンでストーリーを生成
if st.button('ストーリーを生成'):
    if protagonist:
        # ストーリーの概要を生成
        outline = generate_story_outline(genre, protagonist, length)
        
        # Groq APIを使用してストーリーを生成
        with st.spinner('Groq APIからストーリーを生成中...'):
            story = get_story_from_groq(outline)
            st.write("生成されたストーリー:")
            st.write(story)
    else:
        st.warning("主人公の設定を入力してください。")
