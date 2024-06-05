from baseprompt import Baseprompt
import os

baseprompt_api_key = os.environ.get("BASEPROMPT_API_KEY")
prompt_id = os.environ.get("PROMPT_ID")
client = Baseprompt(baseprompt_api_key=baseprompt_api_key)

my_prompt = client.get_prompt(prompt_id=prompt_id)
print(my_prompt)
