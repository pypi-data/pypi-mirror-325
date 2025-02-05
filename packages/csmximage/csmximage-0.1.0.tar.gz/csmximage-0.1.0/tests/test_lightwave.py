import unittest
import numpy as np
import cv2
from src.image_gen import CsmxImageGen
from src.lightwave import CsmxLightwave

class TestCsmxLightwave(unittest.TestCase):

    def test_encode_decode_lightwave(self):
        """Ensure lightwave cryptographic encoding is reversible using Fourier watermarking"""
        img, code = CsmxImageGen.generate_auth_image()
        encoded_img = CsmxLightwave.encode_lightwave_signature(img, code)
        decoded_img = CsmxLightwave.decode_lightwave_signature(encoded_img, code)

        # ✅ Use perceptual hashing with relaxed threshold
        self.assertTrue(CsmxLightwave.compare_images(img, decoded_img), "Image verification failed!")

if __name__ == '__main__':
    unittest.main()
