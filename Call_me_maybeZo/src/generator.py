"""Guided token generation module."""

from typing import List
from llm_sdk import Small_LLM_Model  # type: ignore
from .utils import constrained_


def generate_token(
    src: Small_LLM_Model,
    tokens: List[int],
    allowed: List[int]
) -> int:
    """Select the allowed token with the highest logit value."""
    raw_logits = src.get_logits_from_input_ids(tokens)
    masked_logits = constrained_(raw_logits, allowed)

    next_token: int = max(allowed, key=lambda x: masked_logits[x])
    tokens.append(next_token)
    return next_token
