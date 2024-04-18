import os
import json
import requests
from PIL import Image
from openai import OpenAI # type: ignore
import asyncio
from datetime import datetime

# Load configuration
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "config.json")) as file:
    config = json.load(file)

# Set up API key
OPEN_AI_IMAGE_API = os.environ.get("OPEN_AI_IMAGE_API")
print(f"Loaded Image API key: {OPEN_AI_IMAGE_API[:10]}")

# Initialize OpenAI client
client = OpenAI(api_key=OPEN_AI_IMAGE_API)

async def generate_image_filename(prompt):
    response = client.chat.completions.create(
        model=config["imagen"]["filename_model"],
        messages=[
            {"role": "system", "content": "convert the user's text into a three word filename. ie. prompt:An image of a freshly brewed coffee mug on a table. Response:freshly_brewed_coffee"},
            {"role": "user", "content": prompt},
        ]
    )
    filename = datetime.now().strftime("%Y%m%d%H%M%S_") + response.choices[0].message.content + ".png"
    return filename


async def generate_image_url(prompt):
    response = client.images.generate(
        model=config["imagen"]["image_model"],
        prompt=prompt,
        size=config["imagen"]["image_size"],
        quality="standard",
        n=1
    )
    return response.data[0].url

async def generate_image(prompt, save=True):
    image_url = await generate_image_url(prompt)
    image = Image.open(requests.get(image_url, stream=True).raw)
    if save:
        filename = await generate_image_filename(prompt)
        image.save(os.path.join(script_dir, "images", filename))
    return image

async def generate_images(prompts: list, save=True):
    images = await asyncio.gather(*[generate_image(prompt, save=save) for prompt in prompts])
    return images
