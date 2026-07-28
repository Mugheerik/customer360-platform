def test_authenticated_client(authenticated_client):
    response = authenticated_client.get("/api/v1/auth/me")

    assert response.status_code == 200
