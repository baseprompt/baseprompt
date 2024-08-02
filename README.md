# Baseprompt

[Baseprompt](https://ai.baseprompt.dev/) is a no-code platform to build safe & fast AI applications without writing any code.
## Features

- Run workflows

## Installation

To install the package, run the following command:

```
pip install baseprompt
```

# Usage

### Running a workflow
To run a workflow you created on baseprompt.dev, use run_workflow method:

```
import baseprompt as bp

result = bp.run_workflow(
    api_key="your baseprompt api key",
    workflow_id="your workflow id",
    messages=[{"role": "user", "content": "Hey"}]
)

print(result)
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
