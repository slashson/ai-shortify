from config import API_TOKEN, MODEL_NAME, API_URL
import requests

headers = {"Authorization": f"Bearer {API_TOKEN}"}

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

SYSTEM_PROMPT = "You're helpful assistant that shortens the text that i send to you next : "

def send_message_to_model(prompt):
    payload = {
        "messages": [{"role": "user", "content": f'{SYSTEM_PROMPT}{prompt}'}],
        "model": MODEL_NAME
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

print("🤖 DeepSeek Chat | Type 'exit' to quit\n")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("👋 Goodbye!")
#         break

#     try:
#         reply = send_message_to_model(user_input)
#         print("Bot:", reply)
#     except Exception as e:
#         print("❌ Error:", e)