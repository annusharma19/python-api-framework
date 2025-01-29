import requests
import random
from datetime import datetime, timedelta


def get_auth_token(username="admin", password="password123"):
    """
    Obtain an authentication token to use for authorized requests.
    """
    url = "https://restful-booker.herokuapp.com/auth"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()['token']
    else:
        raise Exception("Failed to get auth token.")


def create_booking(data):
    """
    Create a new booking.
    """
    url = "https://restful-booker.herokuapp.com/booking"
    response = requests.post(url, json=data)
    return response


def modify_booking(booking_id, data, token):
    """
    Modify an existing booking with the provided data.
    """
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.put(url, json=data, headers=headers)
    return response


def delete_booking(booking_id, token):
    """
    Delete a booking by its booking ID using authentication token.
    """
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    print(headers)
    response = requests.delete(url)

    return response


def generate_random_dates():
    """
    Generate random check-in and check-out dates.
    """
    checkin_date = datetime.today() + timedelta(days=random.randint(1, 30))
    checkout_date = checkin_date + timedelta(days=random.randint(1, 7))
    return checkin_date.strftime('%Y-%m-%d'), checkout_date.strftime('%Y-%m-%d')


def generate_booking_data(test_name, price, deposit_paid):
    """
    Generate booking data for different test cases.
    """
    checkin, checkout = generate_random_dates()
    return {
        "firstname": test_name,
        "lastname": "Test",
        "totalprice": price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": "Lunch" if test_name == "Test1" else ""
    }
