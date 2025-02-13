import os
from sqldeps.llm_parsers.base import BaseSQLExtractor
from typing import Optional
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

load_dotenv()


class GroqExtractor(BaseSQLExtractor):
    """Groq-based SQL dependency extractor."""

    ENV_VAR_NAME = "GROQ_API_KEY"

    def __init__(
        self,
        model: str = "llama-3.3-70b-versatile",
        params: Optional[dict] = None,
        api_key: Optional[str] = None,
        prompt_path: Optional[Path] = None,
    ):
        """Initialize Groq extractor."""
        super().__init__(model, params, prompt_path=prompt_path)

        api_key = api_key or os.getenv(self.ENV_VAR_NAME)
        if not api_key:
            raise ValueError(
                f"No API key provided. Either pass api_key parameter or set {self.ENV_VAR_NAME} environment variable."
            )

        self.client = Groq(api_key=api_key)

    def _query_llm(self, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompts["system_prompt"]},
                {"role": "user", "content": user_prompt},
            ],
            response_format={
                'type': 'json_object'
            },
            **self.params,
        )

        return response.choices[0].message.content