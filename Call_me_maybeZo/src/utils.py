import json
import re

def llm_extract_parameters(src, user_request, function):
    prompt = f"""
        You are a function calling assistant.

        Function:
        {json.dumps(function, indent=2)}

        User request:
        {user_request}

        Return only the parameters as JSON.

        Output:
        """

    tokens = src.encode(prompt)[0].tolist()

    generated = []

    for _ in range(20):
        logits = src.get_logits_from_input_ids(tokens)

        next_token = max(
            range(len(logits)),
            key=logits.__getitem__
        )

        tokens.append(next_token)
        generated.append(next_token)

    output = src.decode(generated)
    print("VOILA LE OUTPUT : ", output)

    sortie = re.search(r'{.*?\}', output)

    if sortie is None:
        return {}

    return json.loads(sortie.group())


def constrained_(logits, allowed):
    for i in range(len(logits)):
        if i not in allowed:
            logits[i] = float("-inf")

    return logits
