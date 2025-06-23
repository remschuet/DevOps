from fastapi.testclient import TestClient
from unittest.mock import Mock
from app.main import app, get_user_service

client = TestClient(app)

def test_add_with_mock():
    mock = Mock()
    mock.add.return_value = 42
    assert mock.add(1, 2) == 42

def test_read_user_with_mock():
    # Création du mock
    mock_service = Mock()
    mock_service.get_user.return_value = {"id": 1, "name": "Mocked User"}

    # Injection du mock
    app.dependency_overrides[get_user_service] = lambda: mock_service

    # Appel à l’API
    response = client.get("/users/1")

    # Vérifications
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Mocked User"}
    mock_service.get_user.assert_called_once_with(1)

    # Nettoyage
    app.dependency_overrides.clear()
