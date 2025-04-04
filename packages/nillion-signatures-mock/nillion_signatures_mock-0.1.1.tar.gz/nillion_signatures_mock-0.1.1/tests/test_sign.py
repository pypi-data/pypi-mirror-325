import pytest
from decentralised_signing_crypto_mock import key_gen, sign
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def test_sign():
    # Setup
    nodes_and_jwts = [
        {
            "node_url_1": "node1.example.com",
            "node_jwt": "jwt1"
        },
        {
            "node_url_2": "node2.example.com",
            "node_jwt": "jwt2"
        },
        {
            "node_url_3": "node3.example.com",
            "node_jwt": "jwt3"
        }
    ]
    message = "Test message"

    # Generate RSA key for testing
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    # Get key generation result
    key_result = key_gen("EdDSA", nodes_and_jwts)

    # Add store_ids to nodes_jwts_store_ids
    nodes_jwts_store_ids = [
        {**node, "store_id": key_result[i]["store_id"]}
        for i, node in enumerate(nodes_and_jwts)
    ]

    # Test signing with public key
    sign_result = sign("EdDSA", nodes_jwts_store_ids, message, public_key_pem)
    assert "public_key" in sign_result
    assert "shares" in sign_result
    assert isinstance(sign_result["shares"], list)
    assert len(sign_result["shares"]) == 3

    # Test signing without public key
    sign_result_no_key = sign("EdDSA", nodes_jwts_store_ids, message)
    assert "public_key" not in sign_result_no_key
    assert "shares" in sign_result_no_key
    assert isinstance(sign_result_no_key["shares"], list)
    assert len(sign_result_no_key["shares"]) == 3

    # Check shares
    shares = sign_result["shares"]
    assert len(shares) == 3  # Should have 3 shares
    
    # Check each share's structure
    for share_id, share_data in shares.items():
        assert isinstance(share_data, dict)
        assert "algorithm" in share_data
        assert "parameters" in share_data
        assert "encryptedData" in share_data
        assert share_data["algorithm"] == "RSA-OAEP"
        
        # Check parameters
        params = share_data["parameters"]
        assert params["keySize"] == 2048
        assert params["hash"] == "SHA-256"
        assert params["mgf"] == "MGF1"
        
        # Check encrypted data is non-empty string
        assert isinstance(share_data["encryptedData"], str)
        assert len(share_data["encryptedData"]) > 0 