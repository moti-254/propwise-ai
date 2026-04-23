from __future__ import annotations

import json
import logging
import time
from typing import Optional, Dict, Any

from openai import OpenAI

from app.core.settings import settings

logger = logging.getLogger(__name__)


class OpenRouterClient:
    """
    OpenRouter client using OpenAI SDK wrapper.

    OpenRouter exposes an OpenAI-compatible API.

    Benefits:
    - cleaner SDK
    - better future compatibility
    - easier streaming
    - easier tool calling
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url,
        )

        self.model = settings.openrouter_model

    def _request(
        self,
        prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 1000,
        retries: int = 3,
    ) -> Optional[str]:

        for attempt in range(retries):

            try:
                start = time.time()

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    temperature=temperature,
                    max_tokens=max_tokens,
                )

                latency = time.time() - start

                logger.info(
                    "[OpenRouter] latency=%.2fs model=%s",
                    latency,
                    self.model,
                )

                if not response.choices:
                    logger.warning("No choices returned from model")
                    continue

                content = response.choices[0].message.content

                return content

            except Exception as exc:

                logger.warning(
                    "[OpenRouter] attempt=%s failed error=%s",
                    attempt + 1,
                    str(exc),
                )

                time.sleep(1.5 * (attempt + 1))

        logger.error("[OpenRouter] all retries failed")

        return None

    def complete_json(
        self,
        prompt: str,
    ) -> Optional[Dict[str, Any]]:

        response = self._request(prompt)

        if not response:
            return None

        try:
            cleaned = self._clean_json_response(response)

            return json.loads(cleaned)

        except Exception as exc:

            logger.exception(
                "Failed to parse JSON response: %s",
                exc,
            )

            return None

    def complete_text(
        self,
        prompt: str,
    ) -> Optional[str]:

        return self._request(prompt)

    @staticmethod
    def _clean_json_response(response: str) -> str:
        """
        Removes markdown fences from LLM JSON output.
        """

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace("```json", "")

        if response.startswith("```"):
            response = response.replace("```", "")

        response = response.replace("```", "")

        return response.strip()


openrouter_client = OpenRouterClient()