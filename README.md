# Baseprompt

[Baseprompt](https://baseprompt.dev/) is a collaboration tool and secure storage for LLM chain prompts. It allows you test your prompts even while your server is in run.

## Features

- Create new prompts
- Retrieve existing prompts

## Installation

To install the package, run the following command:

```
pip install git+https://github.com/baseprompt/baseprompt.git
```

# Usage

### Retrieving a prompt
To retrieve an existing prompt, use the get_prompt method:

```
from baseprompt import Baseprompt
import os

baseprompt_api_key = os.environ.get("BASEPROMPT_API_KEY")
prompt_id = os.environ.get("PROMPT_ID")
client = Baseprompt(baseprompt_api_key=baseprompt_api_key)

my_prompt = client.get_prompt(prompt_id=prompt_id)
print(my_prompt)
```

### Creating a prompt
To create a new prompt, use the create_prompt method:

```
from baseprompt import Baseprompt
import os

baseprompt_api_key = os.environ.get("BASEPROMPT_API_KEY")
client = Baseprompt(baseprompt_api_key=baseprompt_api_key)

new_prompt = client.create_prompt(prompt="test prompt", mode="personal", model="gpt-4o", name="test name")
print(new_prompt)
```

# Configuration
The Baseprompt class requires an API key for authentication. You can set the API key using environment variables or directly in your code.

### Environment Variables
Set the following environment variables:

- <b>BASEPROMPT_API_KEY</b>: Your Baseprompt API key
- <b>PROMPT_ID</b>: The ID of the prompt you want to retrieve (for the get_prompt example)

### Directly in Code
You can also set the API key directly in your code:

```
client = Baseprompt(baseprompt_api_key="your_baseprompt_api_key")
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
