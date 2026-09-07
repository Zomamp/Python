from typing import Any
from pydantic import BaseModel

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
