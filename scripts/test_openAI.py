import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me the purpose of life of a crystal child",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)
