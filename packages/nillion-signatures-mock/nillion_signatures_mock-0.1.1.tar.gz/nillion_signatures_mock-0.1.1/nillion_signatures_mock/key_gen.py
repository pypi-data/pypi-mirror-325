import secrets
from cryptography.hazmat.primitives.asymmetric import ed25519, ec

def key_gen(sign_scheme: str, nodes_and_jwts: list[dict]) -> list[dict]:
    """
    Generate keys for the specified signature scheme.
    
    Args:
        sign_scheme (str): Either "ECDSA" or "EdDSA"
        nodes_and_jwts (list): List of dicts with node info and JWTs
        example: [
            {
                "node_url_1": "node1.com",
                "node_jwt": "XXXX"
            },
            {
                "node_url_2": "node2.com",
                "node_jwt": "YYYY"
            }
        ]
    
    Returns:
        list: List of dicts with node URLs and store IDs
    """
    # Mock key generation based on signature scheme
    if sign_scheme == "EdDSA":
        private_key = ed25519.Ed25519PrivateKey.generate()
    else:  # ECDSA
        private_key = ec.generate_private_key(ec.SECP256K1())
    
    # Generate mock store IDs
    store_ids = [secrets.token_hex(8) for _ in nodes_and_jwts]
    
    # Create response format
    response = [
        {
            "node_url_" + str(i+1): node["node_url_" + str(i+1)],
            "store_id": store_id
        }
        for i, (node, store_id) in enumerate(zip(nodes_and_jwts, store_ids))
    ]
    
    return response 