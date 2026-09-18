"""Data models for Function Calling and evaluation schemas."""

from typing import Any, Optional
from pydantic import BaseModel, ConfigDict


class FunctionDefinition(BaseModel):
    """Schema representing a function declaration."""

    name: str
    description: str
    parameters: dict[str, dict[str, Any]]
    returns: dict[str, Any]
    model_config = ConfigDict(extra='forbid')


class FunctionPrompt(BaseModel):
    """Input prompt format."""

    prompt: str
    model_config = ConfigDict(extra='forbid')


class FunctionCall(BaseModel):
    """Output format representing a generated function call."""

    prompt: str
    name: Optional[str]
    parameters: dict[str, Any]
    model_config = ConfigDict(extra='forbid')
