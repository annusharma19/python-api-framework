import pytest
import logging
from utils.api_helper import create_booking, modify_booking, delete_booking, generate_booking_data, get_auth_token
from utils.logger import setup_logger

# Setting up logger for logging the test results
logger = setup_logger()


@pytest.fixture
def setup_bookings():
    """
    Fixture to create 3 new bookings for the tests.
    """
    bookings = []
    for i in range(1, 4):
        test_data = generate_booking_data(f"Test{i}", 500 + (i * 500), i != 3)
        response = create_booking(test_data)
        booking_id = response.json()['bookingid']
        bookings.append(booking_id)
    return bookings


def test_generate_bookings(setup_bookings):
    """
    Test case to generate 3 bookings and log the booking IDs and details.
    """
    logger.info(f"Available Booking IDs: {setup_bookings}")
    for booking_id in setup_bookings:
        logger.info(f"Booking ID {booking_id} created")


def test_modify_bookings(setup_bookings):
    """
    Test case to modify the total price of the bookings (test1 and test2).
    """
    token = get_auth_token()  # Fetch auth token

    logger.info(f"Modifying Booking ID {setup_bookings[0]} to have total price 1000")
    modify_booking(setup_bookings[0], {"totalprice": 1000}, token)

    logger.info(f"Modifying Booking ID {setup_bookings[1]} to have total price 1500")
    modify_booking(setup_bookings[1], {"totalprice": 1500}, token)


def test_delete_booking(setup_bookings):
    """
    Test case to delete one booking and log the return status.
    """
    token = get_auth_token()  # Fetch auth token
    #logger.info(f"available bookings ID {setup_bookings} going to delete with status code {setup_bookings[0]}")
    booking_id_to_delete = setup_bookings[0]
    response = delete_booking(booking_id_to_delete, token)
    logger.info(f"Booking ID {booking_id_to_delete} deleted")
