import baseprompt as bp

result = bp.run_workflow(
    api_key="your baseprompt api key",
    workflow_id="your workflow id",
    messages=[{"role": "user", "content": "Hey"}]
)

print(result)