from PIL import Image
import numpy as np
import os

class CsmxImage:
    """Encrypts data inside images using AI-proof pixel manipulation"""

    @staticmethod
    def embed_text_in_image(text: str, image_path: str, output_path: str):
        """Hides text inside an image by modifying pixel values"""
        if not os.path.exists(image_path):
            img = Image.new("RGB", (500, 500), "white")
            img.save(image_path)

        img = Image.open(image_path)
        img_array = np.array(img)

        binary_text = ''.join(format(ord(char), '08b') for char in text)
        index = 0

        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                if index < len(binary_text):
                    img_array[i, j, 0] = (img_array[i, j, 0] & ~1) | int(binary_text[index])
                    index += 1

        new_img = Image.fromarray(img_array)
        new_img.save(output_path)

    @staticmethod
    def extract_text_from_image(image_path: str) -> str:
        """Extracts hidden text from an encrypted image"""
        img = Image.open(image_path)
        img_array = np.array(img)

        binary_text = ""
        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                binary_text += str(img_array[i, j, 0] & 1)

        text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
        return text.strip()
