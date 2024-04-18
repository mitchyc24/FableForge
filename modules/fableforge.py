import os
import json
from imagen import imagen
from pagen import pagen
from storygen import storygen
import asyncio


class FableForge:
    def __init__(self):
        self.name = "FableForge"
        self.description = "A simple text-based game engine."
        self.version = "0.1.0"
        self.author = "Carroll Compute"
        self.settings = self.load_settings()

    
    def load_settings(self):
        with open("settings.json") as file:
            settings = json.load(file)
        return settings
    
    
    def run(self):
        print("Welcome to FableForge!")
        prompt = input("Describe the story you would like to create:\n")
        self.prompt = prompt
        self.story = asyncio.run(storygen.generate_story(prompt, length=self.settings["story_length"]))
        self.pages = asyncio.run(pagen.generate_pages(self.story, num_pages=self.settings["num_pages"]))
        self.image_prompts = asyncio.run(imagen.pages_to_prompts(self.pages))
        self.images = asyncio.run(imagen.generate_images(self.image_prompts, style=self.settings["image_style"]))


    def save(self):
        title = input("Enter a title for your story:\n")

        # Sanitize the title to remove problematic characters
        safe_title = "".join([c for c in title if c.isalnum() or c in " _-"]).rstrip()

        # Create directory with story title, handling existing directories
        directory_path = os.path.join("forged_stories", safe_title)
        os.makedirs(directory_path, exist_ok=True)

        # Save story, pages, and images in the directory
        try:
            with open(os.path.join(directory_path, "story.txt"), "w") as file:
                file.write(self.story)

            for i, page in enumerate(self.pages):
                with open(os.path.join(directory_path, f"page_{i}.txt"), "w") as file:
                    file.write(page)

            for i, image in enumerate(self.images):
                image.save(os.path.join(directory_path, f"image_{i}.png"))

            print(f"Story saved to {directory_path}")

        except Exception as e:
            print(f"An error occurred while saving the story: {e}")


if __name__ == "__main__":
    forge = FableForge()
    forge.run()
    forge.save()