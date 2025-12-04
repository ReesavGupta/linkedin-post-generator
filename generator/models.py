from pydantic import SecretStr
from langchain_openai import ChatOpenAI
from config import config

if not config["openai_api_key"]:
    raise ValueError("No api key for openai")

openai = ChatOpenAI(
    api_key= SecretStr(config["openai_api_key"]),
    model="gpt-4o",
    stream_usage=True,
    temperature=0.7,
    # reasoning_effort="low",
)
