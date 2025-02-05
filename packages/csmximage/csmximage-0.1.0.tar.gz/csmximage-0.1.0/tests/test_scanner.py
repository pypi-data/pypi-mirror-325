import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from src.lightwave import CsmxLightwave

class CsmxScanner:
    """AI-Powered Image Scanning & Verification"""

    @staticmethod
    def scan_image(image, expected_code):
        """Scans and verifies authentication images using structural similarity"""

        # 🔹 Extract the original image from encoded lightwave signature
        extracted_image = CsmxLightwave.decode_lightwave_signature(image, expected_code)

        # 🔹 Convert images to grayscale for SSIM comparison
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_extracted = cv2.cvtColor(extracted_image, cv2.COLOR_BGR2GRAY)

        # 🔹 Compute Structural Similarity Index (SSIM)
        similarity_score = ssim(gray_image, gray_extracted)

        # ✅ Allow authentication if images have >95% structural similarity
        return similarity_score > 0.95
