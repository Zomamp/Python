from typing import Any
import sys
try:
    from pydantic import BaseModel
except Exception as e:
    print(e)
    sys.exit(1)


class Function_definition(BaseModel):
    """Description anle zavatra ilaina rehetra aloha"""
    name: str
    description: str
    parameters: dict[str, dict[str, Any]]
    returns: dict[str, Any]


class FunctionPrompt(BaseModel):
    """Just a prompt keys in the dict"""
    prompt: str


class FunctionCall(BaseModel):
    """Represent a generated function call."""
    prompt: str
    name: str | None
    parameters: dict[str, Any]
