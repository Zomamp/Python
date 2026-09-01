def llm_extract_parameters(user_request, function_name):
    ex = '{"prompt": "What is the sum of 265 and 345?",' \
            '"name": "fn_add_numbers", "parameters": {"a": 265.0, "b": 345.0}}'
    prompt = f"""
        Your task is to select the appropriate function from the available functions
        and extract its arguments from the user's request.

        Available functions:
        {function_name}

        Example:
        User request: 'what's the sum of 2 and 3'
        Output: {ex}

        User request: {user_request}

        Output:
        """
    return prompt


def constrained_(logits, allowed):
    for i in range(len(logits)):
        if i not in allowed:
            logits[i] = float("-inf")

    return logits
