def test_joker(test_client) -> None:
    response = test_client.get(
        "/api/v1/joke/golf",
        headers={"token": "example_key"},
    )
    assert response.status_code == 200
    assert "joke" in response.json()
