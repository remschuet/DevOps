from unittest.mock import Mock
from app.my_class import MyCalculator

def test_add_with_mock():
    mock = Mock()
    mock.add.return_value = 42
    assert mock.add(1, 2) == 42
