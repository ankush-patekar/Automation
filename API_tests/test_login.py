

def test_login_token(api_client):
    print(api_client.token)
    assert api_client.token is not None
