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

def sign(signature_scheme: str, nodes_jwts_store_ids: list[dict], message: str, public_key: str | None = None) -> dict:
    """
    Sign a message and return encrypted shares.

    Args:
        signature_scheme (str): Either "ECDSA" or "EdDSA"
        nodes_jwts_store_ids (list): List of dicts with node info, JWTs & store_ids
        example: [
            {
                "node_url_1": "node1.com",
                "node_jwt": "XXXX",
                "store_id": "YYYY"
            },
            {
                "node_url_2": "node2.com",
                "node_jwt": "YYYY",
                "store_id": "YYYY"
            }
        ]
        message (str): Message to sign
        public_key (str | None): public key for shares to be (optionally) encrypted

    Returns:
        dict: Public key (if provided) and (encrypted) shares of signed message
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
    shares = create_mock_shares(signature, len(nodes_jwts_store_ids))
    
    # Format response
    response = {
        "shares": [f"share{i+1}" for i in range(len(shares))]
    }
    
    # Add public key if provided
    if public_key:
        response["public_key"] = public_key
    
    return response 