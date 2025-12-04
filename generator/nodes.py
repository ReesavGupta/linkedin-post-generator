from langchain_core.messages import SystemMessage, HumanMessage
from dataclasses import dataclass
from enum import Enum
from models import openai
from prompts import GENERATE_POST_PROMPT

class Niche(Enum):
    AI_ML = 1
    FULL_STACK_DEV = 2
    BLOCKCHAIN = 3

NICHE_LABELS = {
    Niche.AI_ML: "AI/ML",
    Niche.FULL_STACK_DEV: "Full Stack Development",
    Niche.BLOCKCHAIN: "Blockchain"
}

@dataclass
class i_generate_post:
    content: str
    niche: Niche

async def generate_post(input: i_generate_post):
    try:
        if len(input.content) <= 0:
            raise Exception("content needs to be long")
        if not isinstance(input.niche, Niche):
            raise Exception("niche needs to be of proper type")
        
        system_msg = SystemMessage(content=GENERATE_POST_PROMPT)
        human_msg = HumanMessage(
            content=f"Niche: {NICHE_LABELS[input.niche]}, Content: {input.content}"
        )

        messages = [system_msg, human_msg]
        
        async for chunk in openai.astream(messages):
            print(chunk.content, end="", flush=True)

    except Exception as e:
        print("FATAL: something went wriong while generting the post: ", e)
        exit(0)


# if __name__ == "__main__":
#     import asyncio

#     test_input = i_generate_post(
#         content="This is a test post about improving API response times.",
#         niche=Niche.FULL_STACK_DEV
#     )

#     asyncio.run(generate_post(test_input))


# your branch to mine --> master