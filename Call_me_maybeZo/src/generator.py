from utils import constrained_
from llm_sdk import Small_LLM_Model  # type: ignore
from typing import Any


def generate_token(src: Small_LLM_Model, tokens: Any, allowed: Any) -> Any:
    logits = src.get_logits_from_input_ids(tokens)
    logits = constrained_(logits, allowed)

    next_token = max(
        allowed,
        key=lambda x: logits[x]
    )

    tokens.append(next_token)
    return next_token
