from typing import TypedDict


class State(TypedDict):
    user_input: str
    generator: str
    evaluators: list[str]
    generated_post: str
    evaluations: dict[str, str]
    user_accepted: bool
    user_feedback: str