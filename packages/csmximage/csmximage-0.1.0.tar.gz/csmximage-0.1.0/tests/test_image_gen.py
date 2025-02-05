import unittest
import cv2
from src.image_gen import CsmxImageGen

class TestCsmxImageGen(unittest.TestCase):

    def test_generate_auth_image(self):
        """Ensure AI-based image generation is unique and valid"""
        img1, code1 = CsmxImageGen.generate_auth_image()
        img2, code2 = CsmxImageGen.generate_auth_image()
        self.assertNotEqual(code1, code2)  # ✅ Unique codes must be generated

if __name__ == '__main__':
    unittest.main()
