import sys
sys.path.append('/home/mitchell/Github/FableForge/modules')


import unittest
from unittest.mock import patch, mock_open, MagicMock
from modules.fableforge import FableForge 
from PIL import Image




class TestFableForge(unittest.TestCase):
    def test_save_function(self):
        # Setup dummy data
        story = "Once upon a time..."
        pages = ["Page one content", "Page two content"]
        images = [MagicMock(spec=Image.Image), MagicMock(spec=Image.Image)]

        # Setup the FableForge instance
        forge = FableForge()
        forge.story = story
        forge.pages = pages
        forge.images = images

        with patch('builtins.input', return_value="Test Story"), \
             patch('os.makedirs') as mock_makedirs, \
             patch('builtins.open', mock_open()) as mocked_file, \
             patch.object(Image.Image, 'save') as mock_image_save:

            # Run the save method
            forge.save()

            # Assertions to check that the expected calls are made
            mock_makedirs.assert_called_once_with('forged_stories/Test_Story', exist_ok=True)
            self.assertEqual(mocked_file.call_count, 3)  # Opened story.txt, page_0.txt, and page_1.txt
            self.assertEqual(mock_image_save.call_count, 2)  # Two images saved

            # Check that writes were called with correct data
            mocked_file().write.assert_any_call("Once upon a time...")
            mocked_file().write.assert_any_call("Page one content")
            mocked_file().write.assert_any_call("Page two content")

            # Output check
            print("Test complete - Save function passed.")

if __name__ == "__main__":
    unittest.main()
