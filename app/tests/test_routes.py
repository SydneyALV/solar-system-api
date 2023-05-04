def test_read_all_planets_returns_empty_list(client):
    response = client.get("/planets")
    response_body = response.get_json()
    assert response_body == []
    assert response.status_code == 200
    
    
def test_read_planet_by_id(client, make_two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pizza",
        "description": "very chessy",
        "moon count": 8
    }