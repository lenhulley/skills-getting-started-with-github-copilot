"""Tests for the activities listing endpoint."""


def test_get_activities_returns_success_and_dict(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) > 0


def test_get_activities_returns_expected_fields_per_activity(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for details in payload.values():
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
