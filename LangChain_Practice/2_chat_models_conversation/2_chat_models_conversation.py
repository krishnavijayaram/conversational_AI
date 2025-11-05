from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # To make content of the .env file available

load_dotenv()

import os
api_key = os.getenv("GEMINI_API_KEY")
print("API Key ",api_key)
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key=api_key)

messages = [
    SystemMessage("You are an expert in social media content strategy"),
    HumanMessage("Give a short tip to create engaging post on Instagram")
]

result = llm.invoke(messages)

print(result.content)