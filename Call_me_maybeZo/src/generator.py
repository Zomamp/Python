from utils import constrained_


def generate_token(src, tokens, allowed):
    logits = src.get_logits_from_input_ids(tokens)
    logits = constrained_(logits, allowed)

    next_token = max(
        range(len(logits)),
        key=logits.__getitem__
    )

    tokens.append(next_token)

    return next_token

# TESTING OF ONE FUNCTION
def generate_fixed_text(src, tokens, text):
    """Generate a predefined text using constrained decoding."""
    target_tokens = src.encode(text)

    for token_id in target_tokens:
        logits = src.get_logits_from_input_ids(tokens)

        logits = constrained_(
            logits,
            [token_id]
        )

        next_token = max(
            range(len(logits)),
            key=logits.__getitem__
        )

        tokens.append(next_token)