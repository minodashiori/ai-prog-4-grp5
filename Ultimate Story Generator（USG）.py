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

# ストーリーの詳細なプロンプトを生成する関数
def generate_detailed_prompt(genre, protagonist, trait, setting, challenge, ending):
    prompt = f"ジャンル: {genre}\n"
    prompt += f"主人公: {protagonist}\n"
    prompt += f"特徴: {trait}\n"
    prompt += f"背景: {setting}\n"
    prompt += f"挑戦: {challenge}\n"
    prompt += f"結末: {ending}\n"
    prompt += "この情報に基づいて魅力的な物語を生成してください。"
    return prompt

# Groq APIを使用してストーリーの詳細を生成
def get_story_from_groq(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title('ストーリー生成アプリ')

# 各項目をユーザーが入力できるように設定
genre = st.selectbox("ジャンル", ["ファンタジー", "SF", "ロマンス", "ミステリー", "アドベンチャー"])
protagonist = st.text_input("主人公の設定（例: 勇敢な騎士、天才科学者）")
trait = st.text_input("主人公の特徴（例: 最強、優しい、暗い過去を持つ）")
setting = st.text_input("物語の背景（例: 中世の王国、未来の宇宙船）")
challenge = st.text_input("主人公が直面する問題や敵（例: 邪悪なドラゴン、謎の陰謀）")
ending = st.selectbox("物語の結末", ["ハッピーエンド", "バッドエンド", "オープンエンド"])

# ボタンでストーリーを生成
if st.button('ストーリーを生成'):
    if protagonist and genre and trait and setting and challenge:
        # ストーリーのプロンプトを生成
        prompt = generate_detailed_prompt(genre, protagonist, trait, setting, challenge, ending)
        
        # Groq APIを使用してストーリーを生成
        with st.spinner('物語を生成中...'):
            story = get_story_from_groq(prompt)
            st.write(story)  # シンプルにストーリーのみを表示

            # 編集オプション
            edited_story = st.text_area("生成された物語を編集する", story)
            if st.button("編集内容を保存"):
                st.success("物語が保存されました")
                st.write(edited_story)
    else:
        st.warning("すべてのフィールドを入力してください。")
