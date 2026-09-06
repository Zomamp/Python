import json
import re

def llm_extract_parameters(src, user_request, function):
    prompt = f"""
        Extract the arguments from the user request.

        Do NOT execute the function.
        Do NOT calculate the result.
        Do NOT transform the values.

        Function definition:
        {json.dumps(function, indent=2)}

        User request:
        {user_request}

        Return only the arguments as JSON.

        Output:
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

    output = src.decode(generated)

    sortie = re.search(r'{.*?\}', output)

    if sortie is None:
        return {}

    return json.loads(sortie.group())


def constrained_(logits, allowed):
    for i in range(len(logits)):
        if i not in allowed:
            logits[i] = float("-inf")

    return logits
