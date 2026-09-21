"""Main entrypoint for function calling execution."""

import argparse
import json
import sys
from typing import Any, Dict, List
from pydantic import ValidationError
from llm_sdk import Small_LLM_Model  # type: ignore

from .generator import generate_token
from .models import FunctionCall, FunctionPrompt, FunctionDefinition
from .utils import llm_extract_parameters
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--functions_definition',
        type=str,
        default="./data/input/functions_definition.json",
    )
    parser.add_argument(
        '--input',
        type=str,
        default="./data/input/function_calling_tests.json",
    )
    parser.add_argument(
        '--output',
        type=str,
        default="./data/output/function_calling_results.json",
    )

    return parser.parse_args()


def main() -> None:
    """Execute the full function calling pipeline."""
    try:
        src = Small_LLM_Model()
        args = parse_arguments()

        try:
            with open(args.functions_definition, "r", encoding="utf-8") as f:
                raw_function: List[Dict[str, Any]] = json.load(f)
            functions = [
                FunctionDefinition(**func_def) for func_def in raw_function
                ]

            with open(args.input, "r", encoding="utf-8") as f:
                user_requests: List[Dict[str, Any]] = json.load(f)

        except (FileNotFoundError, json.JSONDecodeError) as err:
            print(f"Error reading input files: {err}")
            sys.exit(1)
        except ValidationError as e:
            for er in e.errors():
                print(er['msg'])
                sys.exit(1)
        function_tokens: Dict[str, List[int]] = {}
        for func in functions:
            name = func.name
            function_tokens[name] = src.encode(name)[0].tolist()

        results: List[Dict[str, Any]] = []

        for item in user_requests:
            try:
                prompt_pydantic = FunctionPrompt(**item)
                user_request = prompt_pydantic.prompt
            except ValidationError as e:
                for i in e.errors():
                    print(i['msg'])

            if not user_request:
                empty_call: Dict[str, Any] = {
                    "prompt": user_request,
                    "name": None,
                    "parameters": {}
                }
                results.append(empty_call)
                continue

            prompt = (
                f"Functions: {json.dumps(raw_function)}\n"
                f"User request: {user_request}\n"
                "Function name:"
            )
            tokens = src.encode(prompt)[0].tolist()

            first_tokens = {ids[0] for ids in function_tokens.values()}
            next_token = generate_token(src, tokens, list(first_tokens))

            candidates = [
                (name, ids)
                for name, ids in function_tokens.items()
                if ids[0] == next_token
            ]

            position = 1
            while len(candidates) > 1:
                allowed_next = {
                    ids[position]
                    for _, ids in candidates
                    if position < len(ids)
                }

                if not allowed_next:
                    break

                next_token = generate_token(src, tokens, list(allowed_next))
                candidates = [
                    (name, ids)
                    for name, ids in candidates
                    if position < len(ids) and ids[position] == next_token
                ]
                position += 1

            if not candidates:
                continue

            selected_function_name = candidates[0][0]
            selected_function: FunctionDefinition | None = next(
                (f for f in functions if f.name == selected_function_name),
                None
            )

            if not selected_function:
                continue

            parameters = llm_extract_parameters(
                src,
                user_request,
                selected_function
            )

            result = FunctionCall(
                prompt=user_request,
                name=selected_function_name,
                parameters=parameters
            )
            results.append(result.model_dump())
            print(f"\033[032m{result}\033[0m")

        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(args.output, "w", encoding="utf-8") as file_output:
            json.dump(results, file_output, indent=2)

    except KeyboardInterrupt:
        print("\nProgram execution stopped by user.")
        sys.exit(0)
    except ValidationError as err:
        print(f"Pydantic Validation Error: {err}")
        sys.exit(1)
    except IndexError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
