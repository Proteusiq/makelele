from makelele.core import messages


def test_auth_using_joker_api_no_apikey_header(test_client) -> None:
    response = test_client.get("/api/v1/joke/golf")
    assert response.status_code == 400
    assert response.json() == {"detail": messages.NO_API_KEY}


def test_auth_using_joker_api_wrong_apikey_header(test_client) -> None:
    response = test_client.get(
        "/api/v1/joke/golf",
        headers={"token": "WRONG_TOKEN"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": messages.AUTH_REQ}
