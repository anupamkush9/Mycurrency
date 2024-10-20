import requests
import json
from django.conf import settings
from .error_logger import log_error

base_url = settings.BASE_URL
api_key = settings.API_KEY

def convert_currency(from_currency, to_currency, amount):
    """
    Calls the CurrencyBeacon API to convert an amount from one currency to another.

    This function sends a GET request to the CurrencyBeacon API with the provided source currency,
    target currency, and amount.

    Args:
        from_currency (str): The code of the currency to convert from (e.g., "USD").
        to_currency (str): The code of the currency to convert to (e.g., "EUR").
        amount (float or str): The amount of money to be converted.

    Returns:
        dict: A dictionary containing the API response data, such as the converted amount and rate, if successful.
              If the API request fails or returns an error, an empty dictionary is returned.
    """
    try:
        url = f"{base_url}/v1/convert?api_key={api_key}"
        payload = json.dumps({
            "from": from_currency,
            "to": to_currency,
            "amount": str(amount)
        })
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        return {}
    except Exception as e:
        log_error(message="Error in convert_currency api call", exception=e)
