from typing import List, Optional, Dict, Any
from pydantic import Field
import requests
from loguru import logger

from airtrain.core.skills import Skill, ProcessingError
from airtrain.core.schemas import InputSchema, OutputSchema
from .credentials import FireworksCredentials
from .models import FireworksMessage, FireworksResponse


class FireworksInput(InputSchema):
    """Schema for Fireworks AI chat input"""

    user_input: str = Field(..., description="User's input text")
    system_prompt: str = Field(
        default="You are a helpful assistant.",
        description="System prompt to guide the model's behavior",
    )
    model: str = Field(
        default="accounts/fireworks/models/deepseek-r1",
        description="Fireworks AI model to use",
    )
    temperature: float = Field(
        default=0.7, description="Temperature for response generation", ge=0, le=1
    )
    max_tokens: Optional[int] = Field(
        default=None, description="Maximum tokens in response"
    )
    context_length_exceeded_behavior: str = Field(
        default="truncate", description="Behavior when context length is exceeded"
    )


class FireworksOutput(OutputSchema):
    """Schema for Fireworks AI output"""

    response: str = Field(..., description="Model's response text")
    used_model: str = Field(..., description="Model used for generation")
    usage: Dict[str, int] = Field(default_factory=dict, description="Usage statistics")


class FireworksChatSkill(Skill[FireworksInput, FireworksOutput]):
    """Skill for interacting with Fireworks AI models"""

    input_schema = FireworksInput
    output_schema = FireworksOutput

    def __init__(self, credentials: Optional[FireworksCredentials] = None):
        """Initialize the skill with optional credentials"""
        super().__init__()
        self.credentials = credentials or FireworksCredentials.from_env()
        self.base_url = "https://api.fireworks.ai/inference/v1"

    def process(self, input_data: FireworksInput) -> FireworksOutput:
        """Process the input using Fireworks AI API"""
        try:
            logger.info(f"Processing request with model {input_data.model}")

            # Prepare messages
            messages = [
                {"role": "system", "content": input_data.system_prompt},
                {"role": "user", "content": input_data.user_input},
            ]

            # Prepare request payload
            payload = {
                "messages": messages,
                "model": input_data.model,
                "context_length_exceeded_behavior": input_data.context_length_exceeded_behavior,
                "temperature": input_data.temperature,
                "n": 1,
                "response_format": {"type": "text"},
                "stream": False,
            }

            if input_data.max_tokens:
                payload["max_tokens"] = input_data.max_tokens

            # Make API request
            response = requests.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                headers={
                    "Authorization": f"Bearer {self.credentials.fireworks_api_key.get_secret_value()}",
                    "Content-Type": "application/json",
                },
            )

            response.raise_for_status()
            response_data = FireworksResponse(**response.json())

            logger.success("Successfully processed Fireworks AI request")

            return FireworksOutput(
                response=response_data.choices[0]["message"]["content"],
                used_model=response_data.model,
                usage={
                    "prompt_tokens": response_data.usage.prompt_tokens,
                    "completion_tokens": response_data.usage.completion_tokens,
                    "total_tokens": response_data.usage.total_tokens,
                },
            )

        except Exception as e:
            logger.exception(f"Fireworks AI processing failed: {str(e)}")
            raise ProcessingError(f"Fireworks AI processing failed: {str(e)}")
