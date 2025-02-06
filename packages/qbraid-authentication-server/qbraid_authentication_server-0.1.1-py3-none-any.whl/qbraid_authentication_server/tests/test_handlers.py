import json


async def test_get_example(jp_fetch):
    # When
    response = await jp_fetch("qbraid-authentication-server", "get-example")

    # Then
    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "data": "This is /qbraid-authentication-server/get-example endpoint!"
    }
    
async def test_get_config(jp_fetch):
    # When
    response = await jp_fetch("qbraid-authentication-server", "qbraid-config")

    # Then
    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "email": None,
        "refreshToken": None,
        "apiKey": None,
        "url":None
    }