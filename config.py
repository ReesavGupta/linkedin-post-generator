
import os
from dotenv import load_dotenv
load_dotenv()
config = {
    "openai_api_key" : os.getenv(key="OPENAI_API_KEY")
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
