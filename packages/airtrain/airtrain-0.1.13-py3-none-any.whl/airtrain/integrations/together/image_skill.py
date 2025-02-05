from typing import Optional, List
from pathlib import Path
from pydantic import Field
from together import Together
import base64
import time

from airtrain.core.skills import Skill, ProcessingError
from airtrain.core.schemas import InputSchema, OutputSchema
from .credentials import TogetherAICredentials
from .image_models_config import get_image_model_config, get_default_image_model


class TogetherAIImageInput(InputSchema):
    """Schema for Together AI image generation input"""

    prompt: str = Field(..., description="Text prompt for image generation")
    model: str = Field(
        default=get_default_image_model(), description="Together AI image model to use"
    )
    steps: int = Field(default=10, description="Number of inference steps", ge=1, le=50)
    n: int = Field(default=1, description="Number of images to generate", ge=1, le=4)
    size: str = Field(
        default="1024x1024", description="Image size in format WIDTHxHEIGHT"
    )
    negative_prompt: Optional[str] = Field(
        default=None, description="Things to exclude from the generation"
    )
    seed: Optional[int] = Field(
        default=None, description="Random seed for reproducibility"
    )


class GeneratedImage(OutputSchema):
    """Individual generated image data"""

    b64_json: str = Field(..., description="Base64 encoded image data")
    seed: Optional[int] = Field(None, description="Seed used for this image")
    finish_reason: Optional[str] = Field(
        None, description="Reason for finishing generation"
    )
    url: Optional[str] = Field(None, description="URL of the generated image")


class TogetherAIImageOutput(OutputSchema):
    """Schema for Together AI image generation output"""

    images: List[GeneratedImage] = Field(..., description="List of generated images")
    model: str = Field(..., description="Model used for generation")
    prompt: str = Field(..., description="Original prompt used")
    total_time: float = Field(..., description="Time taken for generation in seconds")
    usage: dict = Field(default_factory=dict, description="Usage statistics")


class TogetherAIImageSkill(Skill[TogetherAIImageInput, TogetherAIImageOutput]):
    """Skill for generating images using Together AI"""

    input_schema = TogetherAIImageInput
    output_schema = TogetherAIImageOutput

    def __init__(self, credentials: Optional[TogetherAICredentials] = None):
        """Initialize the skill with optional credentials"""
        super().__init__()
        self.credentials = credentials or TogetherAICredentials.from_env()
        self.client = Together(
            api_key=self.credentials.together_api_key.get_secret_value()
        )

    def process(self, input_data: TogetherAIImageInput) -> TogetherAIImageOutput:
        try:
            # Validate the model exists in our config
            get_image_model_config(input_data.model)

            start_time = time.time()

            # Generate images
            response = self.client.images.generate(
                prompt=input_data.prompt,
                model=input_data.model,
                steps=input_data.steps,
                n=input_data.n,
                size=input_data.size,
                negative_prompt=input_data.negative_prompt,
                seed=input_data.seed,
            )

            # Calculate total time
            total_time = time.time() - start_time

            # Debug print the response structure
            print(f"Response type: {type(response)}")
            print(f"Response data type: {type(response.data)}")
            if response.data:
                print(f"First image type: {type(response.data[0])}")
                print(f"First image attributes: {dir(response.data[0])}")

            # Convert response to our output format
            generated_images = []
            for img in response.data:
                # Try different possible attribute names for image data
                b64_data = None
                for attr in ["b64_json", "image", "base64", "data"]:
                    if hasattr(img, attr):
                        b64_data = getattr(img, attr)
                        if b64_data:
                            break

                if not b64_data:
                    # If no direct attribute found, try accessing as dictionary
                    try:
                        if hasattr(img, "__dict__"):
                            img_dict = img.__dict__
                            for key in ["b64_json", "image", "base64", "data"]:
                                if key in img_dict and img_dict[key]:
                                    b64_data = img_dict[key]
                                    break
                    except:
                        pass

                if not b64_data:
                    raise ProcessingError(
                        f"No image data found in API response. Response structure: {dir(img)}"
                    )

                generated_images.append(
                    GeneratedImage(
                        b64_json=b64_data,
                        seed=getattr(img, "seed", None),
                        finish_reason=getattr(img, "finish_reason", None),
                        url=getattr(img, "url", None),
                    )
                )

            return TogetherAIImageOutput(
                images=generated_images,
                model=input_data.model,
                prompt=input_data.prompt,
                total_time=total_time,
                usage=getattr(response, "usage", {}),
            )

        except Exception as e:
            raise ProcessingError(f"Together AI image generation failed: {str(e)}")

    def save_images(
        self, output: TogetherAIImageOutput, output_dir: Path
    ) -> List[Path]:
        """
        Save generated images to disk

        Args:
            output (TogetherAIImageOutput): Generation output containing images
            output_dir (Path): Directory to save images

        Returns:
            List[Path]: List of paths to saved images
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        saved_paths = []
        for i, img in enumerate(output.images):
            output_path = output_dir / f"image_{i}.png"
            image_data = base64.b64decode(img.b64_json)

            with open(output_path, "wb") as f:
                f.write(image_data)

            saved_paths.append(output_path)

        return saved_paths
