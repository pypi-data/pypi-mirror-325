from pydantic import SecretStr, BaseModel
from typing import Optional
import os


class FireworksCredentials(BaseModel):
    """Credentials for Fireworks AI API"""

    fireworks_api_key: SecretStr

    @classmethod
    def from_env(cls) -> "FireworksCredentials":
        """Create credentials from environment variables"""
        api_key = os.getenv("FIREWORKS_API_KEY")
        if not api_key:
            raise ValueError("FIREWORKS_API_KEY environment variable not set")

        return cls(fireworks_api_key=api_key)
