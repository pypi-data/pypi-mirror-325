import secrets
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, ed25519
from .encryption import encrypt_share

def create_mock_shares(signature: bytes, num_shares: int) -> list:
    """Create XOR-based secret shares."""
    share_size = len(signature)
    shares = [secrets.token_bytes(share_size) for _ in range(num_shares - 1)]
    
    # Final share is XOR of all shares and signature
    final_share = signature
    for share in shares:
        final_share = bytes(a ^ b for a, b in zip(final_share, share))
    shares.append(final_share)
    
    return shares

def sign(signature_scheme: str, node_info: list, message: str, public_key: str) -> dict:
    """
    Sign a message and create encrypted shares.
    
    Args:
        signature_scheme (str): Either "ECDSA" or "EdDSA"
        node_info (list): List of node URL to store ID mappings
        message (str): Message to sign
        public_key (str): RSA public key in PEM format
    
    Returns:
        dict: Public key and encrypted shares
    """
    # Mock signing operation
    if signature_scheme == "EdDSA":
        private_key = ed25519.Ed25519PrivateKey.generate()
        signature = private_key.sign(message.encode())
    else:  # ECDSA
        private_key = ec.generate_private_key(ec.SECP256K1())
        signature = private_key.sign(
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )

    # Create shares
    shares = create_mock_shares(signature, len(node_info))
    
    # Encrypt shares
    encrypted_shares = {
        f"share{i+1}": encrypt_share(share, public_key)
        for i, share in enumerate(shares)
    }
    
    return {
        "public_key": public_key,
        "shares": encrypted_shares
    } 