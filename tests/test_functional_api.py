from fastapi.testclient import TestClient

from beerlog.api import api


client = TestClient(api)


def test_create_beer_via_api():
    response = client.post(
        "/beers/",
        json={
            "name": "Skoll",
            "style": "KornPA",
            "flavor": 1,
            "image": 2,
            "cost": 3,
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Skoll"
    assert result["id"] == 1
