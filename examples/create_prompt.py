from baseprompt import Baseprompt
import os

baseprompt_api_key = os.environ.get("BASEPROMPT_API_KEY")
client = Baseprompt(baseprompt_api_key=baseprompt_api_key)

new_prompt = client.create_prompt(prompt="test prompt", mode="personal", model="gpt-4o", name="test name")
print(new_prompt)
