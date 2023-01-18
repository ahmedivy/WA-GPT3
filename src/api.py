import os
import openai

openai.api_key = os.environ["OPENAI_KEY"]

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="The best football team in the world is",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)

print(response)
