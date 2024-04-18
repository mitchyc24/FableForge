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
API_KEY = os.environ.get(config["imagen"]["api_key"])

# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)

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

async def generate_image(prompt, style=None, save=True):
    print(f"Generating image for prompt: {prompt}")
    if style:
        prompt = f"{prompt} in the style of {style}"
    image_url = await generate_image_url(prompt)
    image = Image.open(requests.get(image_url, stream=True).raw)
    if save:
        filename = await generate_image_filename(prompt)
        image.save(os.path.join(script_dir, "images", filename))
    return image

async def generate_images(prompts: list, style=None, save=True):
    images = await asyncio.gather(*[generate_image(prompt, style=style, save=save) for prompt in prompts])
    return images


async def pages_to_prompts(pages: list):
    prompts = []
    for page in pages:
        prompt = await page_to_prompt(page)
        prompts.append(prompt)
    return prompts


async def page_to_prompt(page: str):
    response = client.chat.completions.create(
        model=config["imagen"]["page_to_prompt_model"],
        messages=[
            {"role": "system", "content": "convert a page of a story into a suitable image prompt"},
            {"role": "user", "content": page},
        ]
    )
    return response.choices[0].message.content