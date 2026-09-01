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
