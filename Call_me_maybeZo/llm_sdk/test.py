from llm_sdk import Small_LLM_Model
import json
import re


# ============================================================
# EXTRACTION DES PARAMÈTRES
# ============================================================

def extract_parameters(function_name, user_request):
    """
    Extrait les paramètres nécessaires à partir de la requête.
    """

    # --------------------------------------------------------
    # fn_add_numbers
    # --------------------------------------------------------

    if function_name == "fn_add_numbers":

        numbers = re.findall(
            r"-?\d+(?:\.\d+)?",
            user_request
        )

        numbers = [float(number) for number in numbers]

        if len(numbers) >= 2:
            return {
                "a": numbers[0],
                "b": numbers[1]
            }

        return {}

    # --------------------------------------------------------
    # fn_get_square_root
    # --------------------------------------------------------

    if function_name == "fn_get_square_root":

        numbers = re.findall(
            r"-?\d+(?:\.\d+)?",
            user_request
        )

        numbers = [float(number) for number in numbers]

        if len(numbers) >= 1:
            return {
                "a": numbers[0]
            }

        return {}

    # --------------------------------------------------------
    # fn_greet
    # --------------------------------------------------------

    if function_name == "fn_greet":

        match = re.search(
            r"greet\s+(.+)",
            user_request,
            re.IGNORECASE
        )

        if match:
            return {
                "name": match.group(1).strip()
            }

        return {}

    # --------------------------------------------------------
    # fn_reverse_string
    # --------------------------------------------------------

    if function_name == "fn_reverse_string":

        match = re.search(
            r"reverse\s+the\s+string\s+['\"](.+?)['\"]",
            user_request,
            re.IGNORECASE
        )

        if match:
            return {
                "s": match.group(1)
            }

        return {}

    # --------------------------------------------------------
    # fn_substitute_string_with_regex
    # --------------------------------------------------------

    if function_name == "fn_substitute_string_with_regex":

        # Exemple :
        # Replace all numbers in "Hello 34 I'm 233 years old"
        # with NUMBERS

        match = re.search(
            r"replace\s+all\s+numbers\s+in\s+['\"](.+?)['\"]\s+with\s+([A-Za-z0-9_*]+)",
            user_request,
            re.IGNORECASE
        )

        if match:
            return {
                "source_string": match.group(1),
                "regex": r"\d+",
                "replacement": match.group(2)
            }

        # Exemple :
        # Replace all vowels in 'Programming is fun'
        # with asterisks

        match = re.search(
            r"replace\s+all\s+vowels\s+in\s+['\"](.+?)['\"]\s+with\s+([A-Za-z0-9_*]+)",
            user_request,
            re.IGNORECASE
        )

        if match:
            return {
                "source_string": match.group(1),
                "regex": r"[aeiou]",
                "replacement": match.group(2)
            }

        # Exemple :
        # Substitute the word 'cat' with 'dog'
        # in 'The cat sat on the mat with another cat'

        match = re.search(
            r"substitute\s+the\s+word\s+['\"](.+?)['\"]\s+with\s+['\"](.+?)['\"]\s+in\s+['\"](.+?)['\"]",
            user_request,
            re.IGNORECASE
        )

        if match:
            return {
                "source_string": match.group(3),
                "regex": re.escape(match.group(1)),
                "replacement": match.group(2)
            }

        return {}

    return {}


# ============================================================
# CONSTRAINED DECODING
# ============================================================

def constrained_(logits, allowed):
    """
    Garde uniquement les tokens autorisés.
    """

    for i in range(len(logits)):

        if i not in allowed:
            logits[i] = float("-inf")

    return logits


# ============================================================
# GÉNÉRATION D'UN TOKEN
# ============================================================

def generate_token(src, tokens, allowed):

    logits = src.get_logits_from_input_ids(tokens)

    logits = constrained_(
        logits,
        allowed
    )

    next_token = max(
        range(len(logits)),
        key=logits.__getitem__
    )

    tokens.append(next_token)

    return next_token


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    try:

        # --------------------------------------------------------
        # MODEL
        # --------------------------------------------------------

        src = Small_LLM_Model()

        # --------------------------------------------------------
        # FONCTIONS
        # --------------------------------------------------------

        with open(
            "./data/input/functions_definition.json"
        ) as file:

            functions = json.load(file)

        # --------------------------------------------------------
        # REQUÊTES UTILISATEUR
        # --------------------------------------------------------

        with open(
            "./prompt/prompt.json"
        ) as file:

            user_requests = json.load(file)

        # --------------------------------------------------------
        # TOKENS DES NOMS DE FONCTIONS
        # --------------------------------------------------------

        function_tokens = {}

        for function in functions:

            name = function["name"]

            function_tokens[name] = (
                src.encode(name)[0].tolist()
            )

        # --------------------------------------------------------
        # RÉSULTATS
        # --------------------------------------------------------

        results = []

        # ========================================================
        # TRAITEMENT DES REQUÊTES
        # ========================================================

        for item in user_requests:

            user_request = item["prompt"]

            # ----------------------------------------------------
            # PROMPT DU LLM
            # ----------------------------------------------------

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
                "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            )

            print(
                f"\n\033[035mPrompt: {user_request}\033[0m\n"
            )

            # ----------------------------------------------------
            # PREMIERS TOKENS POSSIBLES
            # ----------------------------------------------------

            first_tokens = set()

            for ids in function_tokens.values():

                first_tokens.add(ids[0])

            # ----------------------------------------------------
            # PREMIER TOKEN
            # ----------------------------------------------------

            next_token = generate_token(
                src,
                tokens,
                list(first_tokens)
            )

            # ----------------------------------------------------
            # FONCTIONS COMPATIBLES
            # ----------------------------------------------------

            candidates = []

            for name, ids in function_tokens.items():

                if ids[0] == next_token:

                    candidates.append(
                        (name, ids)
                    )

            # ----------------------------------------------------
            # IDENTIFICATION DE LA FONCTION
            # ----------------------------------------------------

            position = 1

            while len(candidates) > 1:

                allowed = set()

                for name, ids in candidates:

                    if position < len(ids):

                        allowed.add(
                            ids[position]
                        )

                if not allowed:
                    break

                next_token = generate_token(
                    src,
                    tokens,
                    list(allowed)
                )

                new_candidates = []

                for name, ids in candidates:

                    if (
                        position < len(ids)
                        and ids[position] == next_token
                    ):

                        new_candidates.append(
                            (name, ids)
                        )

                candidates = new_candidates

                position += 1

            # ----------------------------------------------------
            # VÉRIFICATION
            # ----------------------------------------------------

            if len(candidates) != 1:

                print(
                    "Impossible de déterminer la fonction."
                )

                continue

            # ----------------------------------------------------
            # FONCTION TROUVÉE
            # ----------------------------------------------------

            function_name = candidates[0][0]

            print(
                f"\033[032mFunction: {function_name}\033[0m"
            )

            # ----------------------------------------------------
            # EXTRACTION DES PARAMÈTRES
            # ----------------------------------------------------

            parameters = extract_parameters(
                function_name,
                user_request
            )

            # ----------------------------------------------------
            # RÉSULTAT
            # ----------------------------------------------------

            result = {
                "prompt": user_request,
                "name": function_name,
                "parameters": parameters
            }

            results.append(result)

            print(
                json.dumps(
                    result,
                    indent=2
                )
            )

        # ========================================================
        # ÉCRITURE DU JSON
        # ========================================================

        with open(
            "./data/output/function_calling_results.json",
            "w"
        ) as file_output:

            json.dump(
                results,
                file_output,
                indent=2
            )

    except KeyboardInterrupt:

        print("\nProgram Stopped")

