import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def welcome_message():
    print("Welcome to AaruNex | Emotional Bridge Project")
    print("Code Accepted: CHAT@AARU@3904")
    print("Please proceed with your emotional input...")

if __name__ == "__main__":
    welcome_message()
