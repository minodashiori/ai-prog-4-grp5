import os
from groq import Groq

# Create the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": "あなたは便利なアシスタントです。質問には簡潔に答えてください。"
}

# Set the user prompt
user_input = "日本で一番高い山は？"
user_prompt = {
    "role": "user", "content": user_input
}

# Initialize the chat history
chat_history = [system_prompt, user_prompt]

response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)

# Print the response
print("Answer:", response.choices[0].message.content)