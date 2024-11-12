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
def generate_detailed_prompt(genre, protagonist, length, trait, setting, challenge):
    prompt = f"ジャンルは{genre}で、主人公は{protagonist}です。物語は{length}で展開されます。"
    prompt += f"\n主人公は「{trait}」という性格や特性を持っており、物語の背景は{setting}です。"
    prompt += f"主人公は{challenge}に直面します。壮大で引き込まれるようなストーリーを作成してください。"
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

# Streamlit UI: プロトタイプデザイン
st.title('📖 ストーリー生成アプリ - プロトタイプ')

# アプリの説明
st.markdown("""
このアプリでは、ジャンルや主人公、ストーリーの長さ、性格、設定、挑戦などを選択して、より具体的なオリジナルの物語を生成します。
""")

# インターフェースのセクション
st.header("📝 ストーリーの設定")

# ジャンル、主人公、ストーリーの長さ、特性、設定、挑戦を選択
genre = st.selectbox("ストーリーのジャンルを選んでください", ["ファンタジー", "SF", "ミステリー", "その他"])
protagonist = st.text_input("主人公の設定を入力してください（例: 勇敢な騎士、天才科学者など）")
length = st.selectbox("ストーリーの長さを選んでください", ["短編", "中編", "長編"])

# 新しい選択式フィールド
trait = st.selectbox("主人公の性格や特性を選んでください", ["誠実", "頭脳明晰", "謎めいた", "大胆不敵"])
setting = st.selectbox("物語の背景を選んでください", ["中世ファンタジーの世界", "未来都市", "魔法の王国", "荒廃した地球"])
challenge = st.selectbox("主人公が直面する挑戦を選んでください", ["世界を救う使命", "過去のトラウマ", "仲間を守る戦い", "禁断の秘密を解く"])

# サイドバーのデザイン（任意）
st.sidebar.header("設定メニュー")
st.sidebar.info("ジャンル、主人公、長さ、特性、設定、挑戦をサイドバーで変更可能です。")

# ボタンでストーリーを生成
if st.button('✨ ストーリーを生成'):
    if protagonist:
        # プロンプトを生成
        prompt = generate_detailed_prompt(genre, protagonist, length, trait, setting, challenge)
        
        # Groq APIを使用してストーリーを生成
        with st.spinner('Groq APIからストーリーを生成中...'):
            story = get_story_from_groq(prompt)
            st.header("🌟 生成されたストーリー")
            st.write(story)
    else:
        st.warning("主人公の設定を入力してください。")

# プロトタイプのデザイン補足
st.markdown("---")
st.subheader("アプリのデザイン概要")
st.markdown("""
- **ジャンル、主人公、長さ、特性、設定、挑戦の選択**: ユーザーが好みの物語の設定を選べます。
- **ストーリー生成ボタン**: 押すとGroq APIでカスタムストーリーが生成されます。
- **サイドバー**: サイドメニューで設定をいつでも変更可能です。
""")
