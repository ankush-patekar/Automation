from API_utils.api_client import APIClient
from API_utils import config
import json


# def test_get_bookings(api_client):   # Fixture reused here
#     response = api_client.get(config.BOOKING_ENDPOINT)
#     assert response.status_code == 200
#     json_data = response.json()
#     json_str = json.dumps(json_data, indent=4)
#     print(json_str)


def test_create_booking(api_client):
    payload = {
        "firstname": "Ath",
        "lastname": "Pat",
        "totalprice": 120,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_client.post(config.BOOKING_ENDPOINT, payload)
    assert response.status_code == 200
    print(response.json())
