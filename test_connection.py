import os
from dotenv import load_dotenv
from anthropic import Anthropic

# read env file
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
model = os.getenv("CLAUDE_MODEL")

client= Anthropic(api_key=api_key)

response = client.messages.create(
model=model,
max_tokens = 100,
messages=[{
    "role":"user" , "content":"say hello in 5 words"}
         ]

)

print(response.content[0].text)

