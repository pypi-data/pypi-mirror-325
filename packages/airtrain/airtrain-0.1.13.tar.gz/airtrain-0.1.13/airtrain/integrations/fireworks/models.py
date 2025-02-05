from typing import List, Optional, Dict, Any
from pydantic import Field, BaseModel


class FireworksMessage(BaseModel):
    """Schema for Fireworks chat message"""

    content: str
    role: str = Field(..., pattern="^(system|user|assistant)$")


class FireworksUsage(BaseModel):
    """Schema for Fireworks API usage statistics"""

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class FireworksResponse(BaseModel):
    """Schema for Fireworks API response"""

    id: str
    choices: List[Dict[str, Any]]
    created: int
    model: str
    usage: FireworksUsage
