import secrets
from cryptography.hazmat.primitives.asymmetric import ed25519, ec

def key_gen(signature_scheme: str, node_urls: list, jwt_token: str) -> dict:
    """
    Generate keys for the specified signature scheme.
    
    Args:
        signature_scheme (str): Either "ECDSA" or "EdDSA"
        node_urls (list): List of node URLs
        jwt_token (str): JWT token for authentication
    
    Returns:
        dict: List of node URL to store ID mappings
    """
    # Mock key generation based on signature scheme
    if signature_scheme == "EdDSA":
        private_key = ed25519.Ed25519PrivateKey.generate()
    elif signature_scheme == "ECDSA":  # ECDSA
        private_key = ec.generate_private_key(ec.SECP256K1())
    else:
        raise ValueError(f"Unsupported signature scheme: {signature_scheme} please select from EdDSA or ECDSA")
    
    # Generate mock store IDs
    store_ids = [secrets.token_hex(8) for _ in node_urls]
    
    # Create response format
    response = {
        "nodes": [
            {url: store_id} for url, store_id in zip(node_urls, store_ids)
        ]
    }
    
    return response 