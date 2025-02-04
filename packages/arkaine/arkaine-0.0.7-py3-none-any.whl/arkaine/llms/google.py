import os
from typing import Optional

import google.generativeai as genai

from arkaine.llms.llm import LLM
from arkaine.tools.agent import Prompt


class Google(LLM):

    CONTEXT_LENGTHS = {
        "gemini-pro": 30720,
        "gemini-1.0-pro": 30720,
        "gemini-1.0-pro-latest": 30720,
        "gemini-1.0-pro-vision": 12288,
        "gemini-1.0-pro-vision-latest": 12288,
    }

    def __init__(
        self,
        model: str = "gemini-pro",
        api_key: Optional[str] = None,
        context_length: Optional[int] = None,
    ):
        if api_key is None:
            api_key = os.environ.get("GOOGLE_AISTUDIO_API_KEY")
            if api_key is None:
                api_key = os.environ.get("GOOGLE_API_KEY")
            if api_key is None:
                raise ValueError(
                    "No Google API key found. Please set "
                    "GOOGLE_AISTUDIO_API_KEY or GOOGLE_API_KEY "
                    "environment variable"
                )

        genai.configure(api_key=api_key)
        self.__model = genai.GenerativeModel(model_name=model)

        if context_length:
            self.__context_length = context_length
        elif model in self.CONTEXT_LENGTHS:
            self.__context_length = self.CONTEXT_LENGTHS[model]
        else:
            raise ValueError(
                f"Unknown model: {model} - must specify context length"
            )

        super().__init__(name=f"gemini:{model}")

    @property
    def context_length(self) -> int:
        return self.__context_length

    def completion(self, prompt: Prompt) -> str:
        # Convert the chat format to Gemini's expected format
        messages = []
        for message in prompt:
            role = message["role"]
            content = message["content"]

            # Map OpenAI roles to Gemini roles
            if role == "system":
                messages.append({"role": "user", "parts": [content]})
            elif role == "assistant":
                messages.append({"role": "model", "parts": [content]})
            elif role == "user":
                messages.append({"role": "user", "parts": [content]})

        # Create a chat session and get response
        chat = self.__model.start_chat()
        response = chat.send_message(
            messages[-1]["parts"][0]
        )  # Send the last message

        return response.text

    def __str__(self) -> str:
        return self.name
