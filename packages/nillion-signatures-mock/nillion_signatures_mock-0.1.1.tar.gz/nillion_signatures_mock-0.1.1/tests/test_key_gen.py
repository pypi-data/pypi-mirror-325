import pytest
from decentralised_signing_crypto_mock import key_gen

def test_key_gen():
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

    # Test EdDSA key generation
    result = key_gen("EdDSA", nodes_and_jwts)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == 3
    
    for node_info in result:
        assert "node_url_" in list(node_info.keys())[0]
        assert "store_id" in node_info

    # Test ECDSA key generation
    result_ecdsa = key_gen("ECDSA", nodes_and_jwts)
    assert isinstance(result_ecdsa, list)
    assert len(result_ecdsa) == 3 