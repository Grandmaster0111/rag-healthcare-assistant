import os
from dotenv import load_dotenv
load_dotenv()

def get_google_api_key():
    return os.getenv("GOOGLE_SEARCH_API_KEY")

def get_google_cx():
    return os.getenv("CX")

def get_gemini_api_key():
    return os.getenv("GEMINI_API_KEY")
