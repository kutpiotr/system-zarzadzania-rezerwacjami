from tests.conftest import client

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API dziala"}

def test_create_user():
    response = client.post(
        "/users/",
        json={
            "name": "Jan",
            "email": "jan@test.pl"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jan"
    assert data["email"] == "jan@test.pl"
    assert "id" in data

def test_create_resource():
    response = client.post(
        "/resources/",
        json={
            "name": "Sala A101",
            "type": "sala"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Sala A101"
    assert data["type"] == "sala"
    assert "id" in data

def test_create_reservation():
    user_response = client.post(
        "/users/",
        json={
            "name": "Piotr",
            "email": "piotr@test.pl"
        }
    )
    user_id = user_response.json()["id"]

    resource_response = client.post(
        "/resources/",
        json={
            "name": "Projektor 1",
            "type": "sprzet"
        }
    )
    resource_id = resource_response.json()["id"]

    reservation_response = client.post(
        "/reservations/",
        json={
            "start_time": "2026-03-08T10:00:00",
            "end_time": "2026-03-08T12:00:00",
            "user_id": user_id,
            "resource_id": resource_id
        }
    )

    assert reservation_response.status_code == 200
    data = reservation_response.json()
    assert data["user_id"] == user_id
    assert data["resource_id"] == resource_id
    assert data["status"] == "pending"

def test_reservation_conflict():
    user_response = client.post(
        "/users/",
        json={
            "name": "Adam",
            "email": "adam@test.pl"
        }
    )
    user_id = user_response.json()["id"]

    resource_response = client.post(
        "/resources/",
        json={
            "name": "Sala B202",
            "type": "sala"
        }
    )
    resource_id = resource_response.json()["id"]

    first_reservation = client.post(
        "/reservations/",
        json={
            "start_time": "2026-03-09T09:00:00",
            "end_time": "2026-03-09T11:00:00",
            "user_id": user_id,
            "resource_id": resource_id
        }
    )

    assert first_reservation.status_code == 200

    second_reservation = client.post(
        "/reservations/",
        json={
            "start_time": "2026-03-09T10:00:00",
            "end_time": "2026-03-09T12:00:00",
            "user_id": user_id,
            "resource_id": resource_id
        }
    )

    assert second_reservation.status_code == 400
    assert second_reservation.json()["detail"] == "Ten zasob jest juz zarezerwowany w tym czasie"