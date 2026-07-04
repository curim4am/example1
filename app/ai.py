from ollama import chat


def ask_ai(text: str) -> str:
    response = chat(
        model="qwen3.5:9b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced SOC analyst. "
                    "Explain security logs in simple language. "
                    "Identify the event, possible risk and recommendation."
                ),
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    )

    return response.message.content