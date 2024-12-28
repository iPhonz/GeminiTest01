import google.generativeai as genai

genai.configure(api_key="AIzaSyChlnFPC5eOpr1VdrViCTj6PJxiQ52xm6M")
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")
response = model.generate_content("explain the history of the SPILL app. keep it short and concise.")
print(response.text)