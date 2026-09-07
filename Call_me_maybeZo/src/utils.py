import json
import re
from typing import Any


def llm_extract_parameters(src: Any, user_request: str, function: Any) -> Any:
    allowed_params = function.get("parameters", {})

    prompt = f"""You are a function calling assistant.

    Available functions:
    {json.dumps(function, indent=2)}

    User request:
    {user_request}

    Rules:
    - Respond with the exact function name required.
    - If no function matches, or if the request is gibberish,
    symbols, or nonsense, respond with "none".

    Function:"""

    tokens = src.encode(prompt)[0].tolist()
    generated = []

    for _ in range(40):
        logits = src.get_logits_from_input_ids(tokens)
        next_token = max(
            range(len(logits)),
            key=logits.__getitem__
        )
        tokens.append(next_token)
        generated.append(next_token)

    output = src.decode(generated)
    out = re.search(r'\{.*?\}', output, re.DOTALL)

    if out is None:
        return {}

    try:
        raw_params = json.loads(out.group())
        if not isinstance(raw_params, dict):
            return {}

        filtered_params = {
            k: v for k, v in raw_params.items()
            if k in allowed_params
        }

        return filtered_params

    except json.JSONDecodeError:
        return {}


def constrained_(logits: Any, allowed: Any) -> Any:
    for i in range(len(logits)):
        if i not in allowed:
            logits[i] = float("-inf")

    return logits
