import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "openai_api_key" : os.getenv(key="OPENAI_API_KEY")
}