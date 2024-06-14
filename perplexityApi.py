import requests
import json


def get_result(prompt):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "llama-3-sonar-large-32k-chat",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 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"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)
    result = data['choices'][0]['message']['content']
    return result