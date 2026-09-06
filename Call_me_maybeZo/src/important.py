from llm_sdk import Small_LLM_Model
import json
from utils import llm_extract_parameters
from generator import generate_token
import models

def main():
    try:
        src = Small_LLM_Model()

        # encodage de fn_add_numbers

        print(src.encode("fn_add_numbers"))

        # Fin de l'encodage
        with open(
            "./data/input/functions_definition.json"
        ) as file:
            functions = json.load(file)

        with open(
            "./data/input/function_calling_tests.json"
        ) as file:
            user_requests = json.load(file)

        function_tokens = {}

        results = []

        print("\033[035m ____  ____  _     _           _      _____      _      ____ ___  _ ____  _____\033[0m\n"
              "\033[036m/   _\\/  _ \\/ \\   / \\         / \\__/|/  __/     / \\__/|/  _ \\\\  \\///  __\\/  __/\033[0m\n"
              "|  /  | / \\|| |   | |   _____ | |\\/|||  \\ _____ | |\\/||| / \\| \\  / | | //|  \\  \n"
              "|  \\__| |-||| |_/\\| |_/\\\\____\\| |  |||  /_\\____\\| |  ||| |-|| / /  | |_\\\\|  /_ \n"
              "\033[035m\\____/\\_/ \\|\\____/\\____/      \\_/  \\|\\____\\     \\_/  \\|\\_/ \\|/_/   \\____/\\____\\\n\033[0m")
        for function in functions:
            name = function["name"]

            function_tokens[name] = (
                src.encode(name)[0].tolist()
            )

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

            candidates = []

            for name, ids in function_tokens.items():

                if ids[0] == next_token:
                    candidates.append((name, ids))

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

                new_candidates = []

                for name, ids in candidates:

                    if (
                        position < len(ids)
                        and ids[position] == next_token
                    ):
                        new_candidates.append((name, ids))

                candidates = new_candidates

                position += 1

            if len(candidates) != 1:
                print("Impossible guy!!!")
                continue

            function_name = candidates[0][0]

            selected_function = None

            for function in functions:
                if function["name"] == function_name:
                    selected_function = function
                    break

            parameters = llm_extract_parameters(
                src,
                user_request,
                selected_function
            )

            result = models.FunctionCall(
                prompt=user_request,
                name=function_name,
                parameters=parameters
            )
            results.append(result.model_dump())

            print(result.model_dump_json(indent=2))

            print(
                "\n\033[032m"
                "██████████████████████████████████████████████████\033[0m"
                )

            with open(
                "./data/output/function_calling_results.json", "w"
                    ) as file_output:
                json.dump(results, file_output, indent=2)
    except KeyboardInterrupt:
        print("\033[031mProgram Stopped\033[0m")
