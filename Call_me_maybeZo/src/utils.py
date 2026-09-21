"""Utility functions for logit masking."""

import json
from typing import Any, Dict, List, Optional
from .models import FunctionDefinition
from llm_sdk import Small_LLM_Model  # type: ignore

ALLOWED_TYPES = {"number", "string", "bool", "float", "integer"}


def constrained_(logits: List[float], allowed: List[int]) -> List[float]:
    """Apply a logit mask to allow only specified token IDs."""
    masked_logits = list(logits)
    allowed_set = set(allowed)
    for i in range(len(masked_logits)):
        if i not in allowed_set:
            masked_logits[i] = float("-inf")
    return masked_logits


def validate_and_cast(val: Any, expected_type: str) -> Optional[Any]:
    """Validate and cast extracted arguments to their expected types."""
    if expected_type not in ALLOWED_TYPES:
        raise ValueError(f"Invalid schema type: '{expected_type}'")

    if val is None:
        return None

    if expected_type == "number":
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            return float(val)
        if isinstance(val, str):
            try:
                num = float(val)
                return num if num.is_integer() else num
            except ValueError:
                return None
        return None

    if expected_type == "integer":
        if isinstance(val, int) and not isinstance(val, bool):
            return int(val)
        if isinstance(val, str):
            try:
                num = int(val)
                return num if num.is_integer() else num
            except ValueError:
                return None
        return None

    elif expected_type == "string":
        if isinstance(val, str):
            return val
        return str(val)

    elif expected_type == "boolean":
        if isinstance(val, bool):
            return val
        if str(val).lower() in ("true", "1"):
            return True
        if str(val).lower() in ("false", "0"):
            return False
        return None

    return val


def llm_extract_parameters(
    src: Small_LLM_Model,
    user_request: str,
    function: FunctionDefinition
) -> Dict[str, Any]:
    """Extract argument values using pure LLM generation and schema casting."""
    allowed_params = function.parameters
    if not allowed_params:
        return {}

    prompt = (
        f"Function: {function.name}\n"
        f"Description: {function.description}\n"
        f"Schema: {json.dumps(allowed_params)}\n"
        f"Query: {user_request}\n\n"
        "Rules:\n"
        "1. Extract parameters matching the schema strictly.\n"
        "2. RegEx patterns MUST use syntax classes:\n"
        r"   - NUMBERS/DIGITS -> '([0-9])+'\\n"
        r"   - VOWELS -> '([aeiouAEIOU])'\\n"
        "3. Output valid JSON object only.\n\n"
        "JSON Arguments:\n{"
    )

    tokens: List[int] = src.encode(prompt)[0].tolist()
    generated: List[int] = []

    for _ in range(60):
        logits = src.get_logits_from_input_ids(tokens)
        next_token = max(range(len(logits)), key=lambda idx: logits[idx])
        tokens.append(next_token)
        generated.append(next_token)

        decoded = src.decode(generated)
        if decoded.rstrip().endswith("}"):
            break

    output = "{" + src.decode(generated).strip()
    raw_params: Dict[str, Any] = {}
    try:
        start_idx = output.find("{")
        end_idx = output.rfind("}")
        if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
            raw_json_str = output[start_idx: end_idx + 1]
            parsed = json.loads(raw_json_str)
            if isinstance(parsed, dict):
                raw_params = parsed
    except json.JSONDecodeError:
        pass

    final_params: Dict[str, Any] = {}
    for key, spec in allowed_params.items():
        expected_type = spec.get("type", "string")
        raw_val = raw_params.get(key)
        final_params[key] = validate_and_cast(raw_val, expected_type)

    return final_params
