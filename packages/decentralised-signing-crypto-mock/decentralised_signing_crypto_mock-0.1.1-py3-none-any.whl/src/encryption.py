import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def encrypt_share(share: bytes, public_key_pem: str) -> dict:
    """
    Encrypt a share using RSA-OAEP.
    
    Args:
        share (bytes): Share to encrypt
        public_key_pem (str): RSA public key in PEM format
    
    Returns:
        dict: Encrypted share with algorithm parameters
    """
    # Load public key
    public_key = serialization.load_pem_public_key(public_key_pem.encode())
    
    # Encrypt the share
    encrypted_data = public_key.encrypt(
        share,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    return {
        "algorithm": "RSA-OAEP",
        "parameters": {
            "keySize": 2048,
            "hash": "SHA-256",
            "mgf": "MGF1"
        },
        "encryptedData": base64.b64encode(encrypted_data).decode()
    } 