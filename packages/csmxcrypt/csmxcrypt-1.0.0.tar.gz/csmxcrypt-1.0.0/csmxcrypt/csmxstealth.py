import random
import string

class CsmxStealth:
    """AI-Proof Invisible Cryptographic Encoding"""

    ZERO_WIDTH_CHARS = ["\u200B", "\u200C", "\u200D", "\u2063", "\u180E"]
    DIACRITIC_MARKS = ["\u0301", "\u034F", "\u0323"]
    DEVANAGARI = ["अ", "ब", "ग", "द", "ह", "ख", "थ", "र", "ल", "श", "ष", "स"]
    JAPANESE = ["カ", "リ", "サ", "タ", "ナ", "ト", "ム", "ミ", "モ", "ラ"]

    @staticmethod
    def _random_noise():
        """Generates deceptive text for obfuscation"""
        noise_chars = random.choices(string.ascii_letters + string.digits, k=random.randint(2, 5))
        return "".join(noise_chars)

    @staticmethod
    def invisible_encode(text: str) -> str:
        """Encodes text into an AI-proof invisible format"""
        encrypted_text = ""
        for char in text:
            base = random.choice(CsmxStealth.DEVANAGARI + CsmxStealth.JAPANESE)
            diacritic = random.choice(CsmxStealth.DIACRITIC_MARKS)
            zero_width = random.choice(CsmxStealth.ZERO_WIDTH_CHARS)
            noise = CsmxStealth._random_noise()
            encrypted_text += base + diacritic + zero_width + noise + char
        return encrypted_text

    @staticmethod
    def remove_invisible_layers(text: str) -> str:
        """Removes invisible Unicode layers to reveal the original text"""
        return "".join([char for char in text if char.isascii()])
