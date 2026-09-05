from llm_sdk import Small_LLM_Model
from json import load
import re
from sys import exit

def generate_constrained_token(
    src: Small_LLM_Model,
    token: list[int],
    allowed: list[int]
) -> int:
    """Generate one token restricted to allowed token IDs."""
    logits = src.get_logits_from_input_ids(token)
    constrained_logits = constraint_decoding(logits, allowed)

    next_token = max(
        range(len(constrained_logits)),
        key=constrained_logits.__getitem__
    )

    token.append(next_token)
    return next_token


# ============================================================
# Choix de la fonction
# Toutes les fonctions commencent par fn_ 8822
# ============================================================

def get_allowed_tokens(function_tokens, prefix):
    """Maka anilay function rehetra , ny token ID anle function rehetra manomboka am 8822 daholo"""
    """De ny ao aoriana no samy hafa arakaraka ny function aminizay"""
    allowed = []

    for tokens in function_tokens.values():
        if tokens[:len(prefix)] == prefix:
            if len(tokens) > len(prefix):
                allowed.append(tokens[len(prefix)])

    return list(set(allowed))


# ============================================================
# Constrained decoding
# ============================================================

def constraint_decoding(logits, allowed):
    """Constrainte decoding kely hitenenana anilay llm hoe ito aloha no alaina"""
    """Ny token rehetra misy vecteur daholo na atsoina hoe score"""
    """Donc ny score plus elever no alainy llm de ataotsika -inf daholo ny score rehetra ankoatrany titsika alaina"""
    constraint_logits = [-float("inf")] * len(logits)

    for ids in allowed:
        constraint_logits[ids] = logits[ids]

    return constraint_logits


# ============================================================
# Extraction des paramètres
# ============================================================

def extract_parameters(user_request, selected_definition):
    """Extract function parameters from the user's request."""
    parameters = selected_definition["parameters"]

    numbers = re.findall(r"-?\d+(?:\.\d+)?", user_request)
    numbers = [float(number) for number in numbers]

    strings = re.findall(r"""['"]([^'"]*)['"]""", user_request)

    result = {}
    number_index = 0
    string_index = 0

    for name, definition in parameters.items():
        parameter_type = definition["type"]

        if parameter_type == "number":
            if number_index < len(numbers):
                result[name] = numbers[number_index]
                number_index += 1

        elif parameter_type == "string":
            if string_index < len(strings):
                result[name] = strings[string_index]
                string_index += 1

    return result


# ============================================================
# MAIN
# ============================================================

def main():

    src = Small_LLM_Model()

    # --------------------------------------------------------
    # Charger les définitions des fonctions
    # --------------------------------------------------------

    with open(
        "./llm_sdk/data/input/functions_definition.json"
    ) as file1:

        function_name = load(file1)

    # --------------------------------------------------------
    # Charger les prompts de test
    # --------------------------------------------------------

    with open(
        "./llm_sdk/data/input/function_calling_tests.json"
    ) as file2:

        calling_prompt = load(file2)

    # ========================================================
    # Traiter chaque prompt
    # ========================================================

    for i in calling_prompt:

        user_request = i["prompt"]

        print("\n" + "=" * 60)
        print("USER :", user_request)
        print("=" * 60)

        # ----------------------------------------------------
        # Exemple de sortie demandée au modèle
        # ----------------------------------------------------

        ex = (
            '{"prompt": "What is the sum of 5 and 5", '
            '"name": "fn_add_numbers", '
            '"parameters": {"a": 5.0, "b": 5.0}}'
        )

        prompt = f"""
            Available functions:
            {function_name}

            The output is like:
            {ex}

            User: {user_request}

            Output:
            """

        # ----------------------------------------------------
        # Encoder le prompt
        # ----------------------------------------------------

        prompt_token = src.encode(prompt)[0].tolist()

        token = prompt_token.copy()

        start_token = len(token)

        # ====================================================
        # ETAT 1 : "prompt"
        # ====================================================

        states_prompt = [
            [src.encode("{")[0].item()],
            [src.encode('"')[0].item()],
            [src.encode("prompt")[0].item()],
            [src.encode('"')[0].item()],
            [src.encode(":")[0].item()],
            [src.encode('"')[0].item()],
        ]

        for allowed in states_prompt:

            logits = src.get_logits_from_input_ids(token)

            logits = constraint_decoding(
                logits,
                allowed
            )

            next_token = max(
                range(len(logits)),
                key=logits.__getitem__
            )

            token.append(next_token)

        # ----------------------------------------------------
        # Ajouter le prompt utilisateur
        # ----------------------------------------------------

        user_request_token = src.encode(
            user_request
        )[0].tolist()

        token.extend(user_request_token)

        # Ajouter le dernier "
        quote_token = src.encode('"')[0].item()
        token.append(quote_token)

        # ====================================================
        # ETAT 2 : "name"
        # ====================================================

        states_name = [
            [src.encode(",")[0].item()],
            [src.encode('"')[0].item()],
            [src.encode("name")[0].item()],
            [src.encode('"')[0].item()],
            [src.encode(":")[0].item()],
            [src.encode('"')[0].item()],
        ]

        for allowed_name in states_name:

            generate_constrained_token(src, token, allowed_name)

        # ====================================================
        # Transformer les noms de fonctions en tokens
        # ====================================================

        function_names = [
            function["name"]
            for function in function_name
        ]

        function_token = {}

        for name in function_names:
            function_token[name] = src.encode(
                name
            )[0].tolist()

        # ====================================================
        # Constrained decoding du nom de fonction
        # ====================================================

        function_prefix = []

        while function_prefix not in function_token.values():

            allowed = get_allowed_tokens(
                function_token,
                function_prefix
            )

            logits = src.get_logits_from_input_ids(token)

            logits = constraint_decoding(
                logits,
                allowed
            )

            next_token = max(
                range(len(logits)),
                key=logits.__getitem__
            )

            token.append(next_token)

            function_prefix.append(next_token)

        # ----------------------------------------------------
        # Trouver le nom correspondant aux tokens générés
        # ----------------------------------------------------

        selected_function = None

        for name, tokens in function_token.items():

            if tokens == function_prefix:
                selected_function = name
                break

        # ====================================================
        # Trouver la définition de la fonction
        # ====================================================

        selected_definition = None

        for function in function_name:

            if function["name"] == selected_function:

                selected_definition = function
        # ================================
                break

        if selected_definition is None:
            print("Error : The function is not here, implement the function")
            continue

        # ----------------------------------------------------
        # Afficher les paramètres attendus
        # ----------------------------------------------------

        parameter_name = list(
            selected_definition["parameters"].keys()
        )


        # ====================================================
        # Extraire les paramètres du prompt
        # ====================================================

        parameters = extract_parameters(
            user_request,
            selected_definition
        )

        # ====================================================
        # ETAT 3 : ,"parameters":{
        # ====================================================

        states_parameters = [
            [src.encode(",")[0].item()],
            [src.encode('"')[0].item()],
            [src.encode("parameters")[0].item()],
            [src.encode('"')[0].item()],
            [src.encode(":")[0].item()],
            [src.encode("{")[0].item()],
        ]

        for allowed_parameter in states_parameters:
            generate_constrained_token(src, token, allowed_parameter)

        # ====================================================
        # Pour l'instant, on génère les noms des paramètres
        # ====================================================

        for index, parameter in enumerate(parameter_name):

            parameter_tokens = src.encode(
                parameter
            )[0].tolist()

            # "

            allowed = [
                src.encode('"')[0].item()
            ]

            logits = src.get_logits_from_input_ids(token)

            logits = constraint_decoding(
                logits,
                allowed
            )

            next_token = max(
                range(len(logits)),
                key=logits.__getitem__
            )

            token.append(next_token)

            # nom du paramètre

            for parameter_token in parameter_tokens:

                allowed = [parameter_token]

                generate_constrained_token(src, token, allowed)

            # "

            allowed = [
                src.encode('"')[0].item()
            ]

            generate_constrained_token(src, token, allowed)

            # :

            allowed = [
                src.encode(":")[0].item()
            ]

            generate_constrained_token(src, token, allowed)

            # =================================================
            # Valeur du paramètre
            # =================================================

            value = parameters.get(parameter)

            if value is None:
                continue

            value_tokens = src.encode(
                str(value)
            )[0].tolist()

            for value_token in value_tokens:

                allowed = [value_token]

                generate_constrained_token(src, token, allowed)

            # -------------------------------------------------
            # Virgule entre les paramètres
            # -------------------------------------------------

            if index < len(parameter_name) - 1:

                allowed = [
                    src.encode(",")[0].item()
                ]

                generate_constrained_token(src, token, allowed)

        # ====================================================
        # Fermer le JSON
        # ====================================================

        closing_tokens = [
            [src.encode("}")[0].item()],
            [src.encode("}")[0].item()],
        ]

        for allowed in closing_tokens:

            generate_constrained_token(src, token, allowed)

        # ====================================================
        # Décoder uniquement ce qui a été généré
        # ====================================================

        generated_token = token[start_token:]

        decodage = src.decode(
            generated_token
        )

        print(decodage)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("\033[031mThe program is Stopping: ", e, "\033[0m")
        exit(1)
    except FileNotFoundError as error:
        print("\033[031mThis File doesn't exit in the repository\033[0m")
        exit(1)
