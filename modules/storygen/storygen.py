import os
import json
from openai import OpenAI # type: ignore


# Load configuration
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "config.json")) as file:
    config = json.load(file)

# Set up API key
API_KEY = os.environ.get(config["storygen"]["api_key"])


# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)


async def generate_story(prompt, length=200):
    print(f"Generating story for prompt: {prompt}")
    response = client.chat.completions.create(
        model=config["storygen"]["model"],
        messages=[
            {"role": "system", "content": f"Write a {length} word story based on the following prompt: "},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content


