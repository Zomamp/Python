from llm_sdk import Small_LLM_Model
import json


def constrained_(logits, allowed):
    for i in range(len(logits)):
        if i not in allowed:
            logits[i] = float("-inf")

    return logits


def generate_token(src, tokens, allowed):
    logits = src.get_logits_from_input_ids(tokens)
    logits = constrained_(logits, allowed)

    next_token = max(
        range(len(logits)),
        key=logits.__getitem__
    )

    tokens.append(next_token)

    return next_token


if __name__ == "__main__":

    try:
        src = Small_LLM_Model()

        with open(
            "./data/input/functions_definition.json"
        ) as file:
            functions = json.load(file)

        with open(
            "./prompt/prompt.json"
        ) as file:
            user_requests = json.load(file)

        # ------------------------------------------------------------
        # Tokens des fonctions
        # ------------------------------------------------------------

        function_tokens = {}

        for function in functions:
            name = function["name"]

            function_tokens[name] = (
                src.encode(name)[0].tolist()
            )

        # ------------------------------------------------------------
        # Traitement
        # ------------------------------------------------------------

        for item in user_requests:

            user_request = item["prompt"]

            if not user_request.strip():
                result = {
                    "prompt": user_request,
                    "name": None,
                    "parameters": {}
            }
                print(json.dumps(result, indent=2))
                continue

            prompt = f"""
                You are a function calling assistant.

                Available functions:
                {json.dumps(functions, indent=2)}

                User request:
                {user_request}

                Choose the correct function.
                """

            tokens = src.encode(prompt)[0].tolist()

            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            print("\n\033[035mPrompt:", user_request, "\n\033[0m")

            # --------------------------------------------------------
            # On regarde les premiers tokens possibles des fonctions
            # --------------------------------------------------------

            first_tokens = set()

            for ids in function_tokens.values():
                first_tokens.add(ids[0])

            # --------------------------------------------------------
            # Génération du premier token du nom
            # --------------------------------------------------------

            generated = []

            next_token = generate_token(
                src,
                tokens,
                list(first_tokens)
            )

            generated.append(next_token)

            # --------------------------------------------------------
            # Trouver les fonctions compatibles
            # --------------------------------------------------------

            candidates = []

            for name, ids in function_tokens.items():

                if ids[0] == next_token:
                    candidates.append((name, ids))

            # --------------------------------------------------------
            # Continuer jusqu'à identifier la fonction
            # --------------------------------------------------------

            position = 1

            while len(candidates) > 1:

                allowed = set()

                for name, ids in candidates:

                    if position < len(ids):
                        allowed.add(ids[position])

                next_token = generate_token(
                    src,
                    tokens,
                    list(allowed)
                )

                generated.append(next_token)

                # garder seulement les fonctions compatibles
                new_candidates = []

                for name, ids in candidates:

                    if (
                        position < len(ids)
                        and ids[position] == next_token
                    ):
                        new_candidates.append((name, ids))

                candidates = new_candidates

                position += 1

            # --------------------------------------------------------
            # Fonction trouvée
            # --------------------------------------------------------

            if len(candidates) != 1:
                print("Impossible de déterminer la fonction.")
                continue

            function_name = candidates[0][0]

            

            # --------------------------------------------------------
            # Pour l'instant : paramètres à déterminer
            # --------------------------------------------------------

            result = {
                "prompt": user_request,
                "name": function_name,
                "parameters": {}
            }

            print(
                json.dumps(
                    result,
                    indent=2
                )
            )
            with open("./data /output/function_calling_results.json", "w") as file_output:
                json.dump(result, file_output, indent=2)
    except KeyboardInterrupt as e:
        print("Program Stopped")