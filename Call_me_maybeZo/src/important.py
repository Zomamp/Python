from llm_sdk import Small_LLM_Model
import json
from utils import llm_extract_parameters
from generator import generate_token


def main():
    try:
        src = Small_LLM_Model()

        # with open(
        #     "./data/output/function_calling_results.json", "w"
        #         ) as file_output:
        #     ...
        with open(
            "./llm_sdk/data/input/functions_definition.json"
        ) as file:
            functions = json.load(file)

        with open(
            "data/input/input.json"
        ) as file:
            user_requests = json.load(file)

        # ------------------------------------------------------------
        # Tokens des fonctions
        # ------------------------------------------------------------

        function_tokens = {}

        # ------------------------------------------------------------
        # Pour aspect JSON
        # ------------------------------------------------------------
        results = []

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
                print(
                    "\n\033[032m"
                    "██████████████████████████████████████████████████\033[0m"
                    )
                print("\n\033[035m👉 Prompt:", user_request, "\n\033[0m")
                result = {
                    "prompt": user_request,
                    "name": None,
                    "parameters": {}
                }

                results.append(result)

                print(
                    json.dumps(
                        result,
                        indent=2
                    )
                )

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

            print(
                "\n\033[032m"
                "██████████████████████████████████████████████████\033[0m"
                )

            print(
                "\n\033[035m👉 Prompt:", user_request, "\n\033[0m"
                )

            first_tokens = set()

            for ids in function_tokens.values():
                first_tokens.add(ids[0])

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
            # --------------------------------------------------------
            # Positionning
            # --------------------------------------------------------
                position += 1

            # --------------------------------------------------------
            # Fonction trouvée
            # --------------------------------------------------------

            if len(candidates) != 1:
                print("Impossible guy")
                continue

            function_name = candidates[0][0]

            parameters = llm_extract_parameters(
                user_request,
                function
            )

            # --------------------------------------------------------
            # Pour l'instant : paramètres à déterminer
            # --------------------------------------------------------

            result = {
                "prompt": user_request,
                "name": function_name,
                "parameters": parameters,
            }
            results.append(result)

            print(
                json.dumps(
                    result,
                    indent=2
                )
            )

            print(
                "\n\033[032m"
                "██████████████████████████████████████████████████\033[0m"
                )

            # with open(
            #     "./data/output/function_calling_results.json", "w"
            #         ) as file_output:
            #     json.dump(results, file_output, indent=2)
    except KeyboardInterrupt:
        print("Program Stopped")
