import requests
from configs.config import BASE_URL, HEADERS
from utils.logger import logger

class BookingPage:
    def create_booking(self, total_price, deposit_paid, additional_needs):
        payload = {
            "firstname": "Test",
            "lastname": "User",
            "totalprice": total_price,
            "depositpaid": deposit_paid,
            "bookingdates": {
                "checkin": "2025-02-01",
                "checkout": "2025-02-10"
            },
            "additionalneeds": additional_needs
        }
        response = requests.post(f"{BASE_URL}/booking", json=payload, headers=HEADERS)

        if response.status_code == 200 or response.status_code == 201:
            booking_id = response.json().get("bookingid")
            logger.info(f"Created booking with ID: {booking_id}")
            return booking_id
        else:
            logger.error(f"Failed to create booking: {response.text}")
            return None

    def modify_booking(self, booking_id, new_price):
        payload = {"totalprice": new_price}
        response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=payload, headers=HEADERS)

        if response.status_code == 200:
            logger.info(f"Booking {booking_id} updated with new price {new_price}")
            return True
        else:
            logger.error(f"Failed to update booking {booking_id}: {response.text}")
            return False

    def delete_booking(self, booking_id):
        response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=HEADERS)

        if response.status_code == 201:
            logger.info(f"Booking {booking_id} successfully deleted")
            return True
        else:
            logger.error(f"Failed to delete booking {booking_id}: {response.text}")
            return False

    def get_all_bookings(self):
        response = requests.get(f"{BASE_URL}/booking")
        if response.status_code == 200:
            bookings = response.json()
            logger.info(f"Fetched {len(bookings)} bookings")
            return [b["bookingid"] for b in bookings]
        else:
            logger.error(f"Failed to fetch bookings: {response.text}")
            return []
