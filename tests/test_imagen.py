import unittest
from modules.imagen import imagen
from PIL import Image

# Unittests
class TestImageGeneration(unittest.IsolatedAsyncioTestCase):

    async def test_generate_single_image(self):
        prompt = "A beautiful sunset"
        image = await imagen.generate_image(prompt)
        self.assertIsInstance(image, Image.Image)
        imagen.save_image(image, await imagen.generate_image_filename(prompt))

    async def test_generate_multiple_images(self):
        prompts = ["A beautiful sunset", "A cute cat", "A portrait of a person"]
        images = await imagen.generate_images(prompts)
        self.assertEqual(len(images), 3)
        for i, image in enumerate(images):
            self.assertIsInstance(image, Image.Image)
            imagen.save_image(image, await imagen.generate_image_filename(prompts[i]))