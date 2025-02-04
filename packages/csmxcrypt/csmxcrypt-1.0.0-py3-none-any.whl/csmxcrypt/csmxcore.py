from csmxcrypt.csmxstealth import CsmxStealth
from csmxcrypt.csmximage import CsmxImage
from csmxcrypt.csmxhash import CsmxHash
from csmxcrypt.csmxkey import CsmxKey
import random
import string

class CsmxCrypt:
    """Main cryptographic engine integrating all encryption modules"""

    @staticmethod
    def _generate_fake_data():
        """Generates AI-proof fake text to confuse pattern recognition models"""
        return "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))

    def secure_data(self, data: str):
        """Encrypts data using multiple layers of security"""
        invisible_text = CsmxStealth.invisible_encode(data)  # 🔥 Invisible Unicode Encryption
        hashed_text = CsmxHash.secure_hash(data)  # 🔥 Quantum-Safe Hash
        CsmxImage.embed_text_in_image(data, "input.png", "output.png")  # 🔥 Hide in Image
        secure_key = CsmxKey.generate_secure_key()  # 🔥 Secure Key Generation
        fake_data = self._generate_fake_data()  # 🔥 Generate false data for AI deception

        return {
            "encrypted_text": fake_data + invisible_text + fake_data,  # AI sees random garbage
            "hashed_text": hashed_text,
            "hidden_in_image": "output.png",
            "secure_key": secure_key
        }
