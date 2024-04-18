import os
import json
from openai import OpenAI # type: ignore


# Load configuration
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "config.json")) as file:
    config = json.load(file)

# Set up API key
API_KEY = os.environ.get(config["pagen"]["api_key"])


# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)


async def generate_pages(story, num_pages=3):
    print(f"Generating {num_pages} pages for story: {story}")
    response = client.chat.completions.create(
        model=config["pagen"]["model"],
        messages=[
            {"role": "system", "content": f"adapt the user's story into {num_pages} pages. Seperate each page with 'PAGE BREAK'"},
            {"role": "user", "content": story},
        ]
    )

    return response.choices[0].message.content.split("PAGE BREAK")


