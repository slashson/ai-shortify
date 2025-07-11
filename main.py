from app import send_message_to_model
import json
import requests

from server import user_text




user_input = user_text
if user_input.lower() in ["exit", "quit"]:
    print("👋 Goodbye!")

try:
    reply = send_message_to_model(user_input)
    print("Bot:", reply)
except Exception as e:
    print("❌ Error:", e)

# while True :
#     user_input = input('You : ')
#     if user_input.lower() in ['quit' 'exit']:
#         print ('Goodbye!')
#         break
#     try:
#         replay = send_message_to_model(user_input)
#         print ('Bot :', replay)
#     except Exception as e:
#         print('Error 404')