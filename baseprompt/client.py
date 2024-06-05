import requests
from .config import Config


class Baseprompt:
    def __init__(self, baseprompt_api_key, openai_api_key=None):
        self.openai_api_key = openai_api_key
        self.baseprompt_api_key = baseprompt_api_key
        self.base_url = Config.API_BASE_URL

    def _openai_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_api_key}"
        }

    def _baseprompt_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.baseprompt_api_key}"
        }

    def set_openai_api_key(self, api_key):
        """Setter for the OpenAI API key"""
        if not api_key:
            raise ValueError("An API key cannot be empty")
        self.openai_api_key = api_key

    def set_baseprompt_api_key(self, api_key):
        """Setter for the Baseprompt API key"""
        if not api_key:
            raise ValueError("An API key cannot be empty")
        self.baseprompt_api_key = api_key

    def set_prompt_id(self, prompt_id):
        """Setter for the prompt ID"""
        self.prompt_id = prompt_id

    def make_request(self, endpoint, method="GET", data=None, baseprompt=False):
        if baseprompt:
            if not self.baseprompt_api_key:
                raise ValueError("A Baseprompt API key is required for making requests")
            url = f"{Config.BASEPROMPT_BASE_URL}/{endpoint}"
            headers = self._baseprompt_headers()
        else:
            if not self.openai_api_key:
                raise ValueError("An OpenAI API key is required for making requests")
            url = f"{self.base_url}/{endpoint}"
            headers = self._openai_headers()

        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_prompt(self, prompt_id):
        endpoint = "get_prompt"

        if not self.baseprompt_api_key:
            raise ValueError("a baseprompt api key is required for making requests")
        if not prompt_id:
            raise ValueError("a sprompt id is required for making requests")

        data = {
            "api_key": self.baseprompt_api_key,
            "prompt_id": prompt_id
        }

        response = self.make_request(endpoint=endpoint, method="POST", data=data, baseprompt=True)
        return response

    def create_prompt(self, prompt, mode="personal", model="gpt-4o", name=None, output=None):
        endpoint = "create_prompt"

        if not self.baseprompt_api_key:
            raise ValueError("A Baseprompt API key is required to make requests")
        if not name:
            raise ValueError("A name is required to create a new prompt")

        data = {
            "api_key": self.baseprompt_api_key,
            "prompt": prompt,
            "type": mode,
            "model": model,
            "name": name,
            "output": output
        }

        response = self.make_request(endpoint=endpoint, method="POST", data=data, baseprompt=True)

        return response
