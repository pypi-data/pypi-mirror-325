import sys
import os

# Ensure Python finds the 'csmxcrypt' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../csmxcrypt')))

from csmxcore import CsmxCrypt  # Now it should work

crypt = CsmxCrypt()

def test_secure_data():
    """Test secure_data() function to ensure encryption works"""
    result = crypt.secure_data("QuantumSecure123")
    assert isinstance(result, dict)
    assert "encrypted_text" in result
    assert "hashed_text" in result
    assert "hidden_in_image" in result
    assert "secure_key" in result
