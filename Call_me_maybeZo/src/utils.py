import json
import re
from typing import Any, Dict, Optional
from llm_sdk import Small_LLM_Model  # type: ignore


def validate_and_cast(val: Any, expected_type: str) -> Optional[Any]:
    """Vérifie et convertit la valeur selon le type attendu dans le JSON."""
    if val is None:
        return None

    if expected_type == "number":
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            return val
        elif isinstance(val, bool):
            return None
        try:
            num = float(val)
            return int(num) if num.is_integer() else num
        except (ValueError, TypeError):
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
        function: Any
        ) -> Dict[str, Any]:
    allowed_params = function.get("parameters", {})
    allowed_keys = list(allowed_params.keys())

    prompt = f"""Extract the argument values
        from the user request for the function.

        Function definition:
        {json.dumps(function, indent=2)}

        CRITICAL: Only use parameter names that exist in the definition
        ({'\n'.join(allowed_keys)}). Do NOT invent new parameters.

        User request:
        {user_request}

        Return ONLY the arguments JSON object:
        """

    tokens = src.encode(prompt)[0].tolist()
    generated = []

    for _ in range(30):
        logits = src.get_logits_from_input_ids(tokens)
        next_token = max(
            range(len(logits)),
            key=logits.__getitem__
        )
        tokens.append(next_token)
        generated.append(next_token)

        if "}" in src.decode([next_token]):
            break

    output = src.decode(generated)
    out = re.search(r'\{.*?\}', output, re.DOTALL)

    raw_params: Dict[str, Any] = {}
    if out is not None:
        try:
            parsed = json.loads(out.group())
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


def constrained_(logits: Any, allowed: Any) -> Any:
    for i in range(len(logits)):
        if i not in allowed:
            logits[i] = float("-inf")

    return logits
