import os

BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}
LOG_FILE = os.path.join(os.getcwd(), "logs", "booking_test.log")
HTML_REPORT = os.path.join(os.getcwd(), "reports", "test_report.html")

# Ensure directories exist
for folder in ["logs", "reports"]:
    if not os.path.exists(folder):
        os.makedirs(folder)
