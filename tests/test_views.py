from unittest.mock import patch

from src.views import api_currency, api_stoks


@patch("requests.get")
def test_api_currency(mock_get):

    mock_get.return_value.json.return_value = {"base": "RUB", "rates": {"USD": 0.012779}}

    assert api_currency() == {"base": "RUB", "rates": {"USD": 0.012779}}


@patch("requests.get")
def test_api_stoks(mock_get):

    mock_get.return_value.json.return_value = {"symbol": "AAPL", "name": "Apple Inc.", "price": 201.56}

    assert api_stoks() == {"symbol": "AAPL", "name": "Apple Inc.", "price": 201.56}
