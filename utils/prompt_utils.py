def clean_prompt(prompt: str) -> str:
    prompt = prompt.strip()
    prompt = prompt.replace("\n", " ")
    return prompt
