import os

def get_google_api_key():
    return os.environ.get("GOOGLE_CSE_API_KEY", "")

def get_google_cx():
    return os.environ.get("GOOGLE_CSE_CX", "")

def get_gemini_api_key():
    return os.environ.get("GEMINI_API_KEY", "")
