from llm_sdk import Small_LLM_Model
import json


if __name__ == "__main__":
    try:
        src = Small_LLM_Model()

        with open("./data/input/functions_definition.json", "r") as file:
            data = json.load(file)

        with open("./prompt/prompt.json", "r") as file:
            user_requests = json.load(file)

        results = []
        ex = '{"name": "fn_add_numbers", "parameters": {"a": {5.0}, "b": {5.0}}, "returns": {"10.0"}}'
        for item in user_requests:

            user_request = item["prompt"]



            prompt = f"""
                Select the function matching the user request.

                The Output must be like the example:
                {ex}
                Functions:
                {json.dumps(data)}

                User request:
                {user_request}

                Return only the JSON object.
                """

            # Tokenisation
            token = src.encode(prompt)[0].tolist()

            stockage = ""
            json_started = False

            # Maximum de tokens générés
            print("\nPrompt: ", item["prompt"], "\n")
            for _ in range(50):

                logits = src.get_logits_from_input_ids(token)

                next_token_id = max(
                    range(len(logits)),
                    key=logits.__getitem__
                )

                token.append(next_token_id)

                decoded = src.decode([next_token_id])

                # Attendre le début du JSON
                if not json_started:
                    if "{" not in decoded:
                        continue

                    json_started = True

                stockage += decoded

                # Essayer de parser le JSON
                try:
                    result = json.loads(stockage)

                    results.append(result)

                    print(
                        f"\033[036m"
                        f"{json.dumps(result, indent=2)}"
                        f"\033[0m"
                    )

                    break

                except json.JSONDecodeError:
                    pass

        # Écrire une seule fois à la fin
        with open("./data/output/function_calling_results.json", "w") as file:
            json.dump(results, file, indent=2)

    except KeyboardInterrupt:
        print("\nThe program stopped.")
