import json
from typing import Dict, List

from openai import OpenAI


class LLMChat:
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o",
        temperature: float = 0.0,
        top_p: float = 1.0,
        show_response: bool = False,
    ):
        self.api = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.show_response = show_response

    def chat(
        self,
        messages: List[Dict[str, str]],
        cast_response_to_json: bool = False,
    ):
        response_data = self.api.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            top_p=self.top_p,
        )

        response = response_data.choices[0].message.content

        if self.show_response:
            print(response)

        if cast_response_to_json:
            response = json.loads(response)

        return response

    def build_system_message(self, system_prompt: str):
        return {"role": "system", "content": system_prompt.replace("\n", "")}

    def build_user_message(self, user_prompt: str):
        return {"role": "user", "content": user_prompt.replace("\n", "")}
