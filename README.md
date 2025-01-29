# Python API Automation Framework

A Python framework for automating interactions with the **Restful Booker API**.

## Prerequisites
- Python 3.x installed

# Clone the repo:
git clone https://github.com/yourusername/python-api-framework.git
cd python-api-framework

# to run tests 
- pytest <path/to/testfile>

# to run tests in verbose mode
- pytest -v -s <path/to/testfile>

## Installation
- **Python 3.11+** required.
- Clone the repo:
    ```bash
    git clone https://github.com/yourusername/booking-api-framework.git
    cd booking-api-framework
    ```
- Install dependencies from `requirements.txt`:
   
    pip install -r requirements.txt
   
- Logs will be stored in `logs/`, and the HTML report will be generated in `reports/`.

## Test Scenarios
1. **Generate 3 New Bookings** – Logs booking details.
2. **Modify Total Price** – Modifies Test1 and Test2 prices.
3. **Delete Booking** – Logs status code.

## HTML Report
- Converts logs to a styled HTML report using `convert_log_to_html.py`.

## Logging
- Logs actions: booking IDs, creation, modification, and deletion.
- Logs are stored in `logs/` directory.

## Github Actions
- python-app.yml file has the required configuration to run github actions on pull/push request.
- artifacts are created post PR "test_log.html" 



