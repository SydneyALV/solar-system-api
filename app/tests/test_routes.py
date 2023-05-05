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
        "moon_count": 8
    }

def test_response_404_for_planet_id_not_found(client, make_two_planets):
    # Arrange
    response = client.get("/planets/3")
    response_body = response.get_json()
    # Act
    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "planet #3 is not found"}

def test_response_400_for_invalid_planet_id(client, make_two_planets):
    # Arrange
    response = client.get("/planets/T")
    response_body = response.get_json()
    # Act
    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "planet #T is not valid"}

def test_create_planet_successfully(client):
    pass
    # Arrange
    # Act
    # Assert

def test_update_planet_successfully(client, make_two_planets):
    pass

def test_delete_planet_successfully(client, make_two_planets):
    pass
