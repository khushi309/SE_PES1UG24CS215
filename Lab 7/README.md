# Lab 7 – Fuzz Testing
## Airline Baggage Fees

### Objective
To perform fuzz testing on the Airline Baggage application
using the Hypothesis property-based testing library.

### Application Functions

1. parse_booking()
   - Parses airline code, flight number and seat letter.
   - Validates booking code format and input values.

2. total_weight()
   - Calculates the total baggage weight from CSV input.
   - Handles invalid, negative and non-finite weights.

3. tag_label()
   - Generates a passenger baggage tag using the
     first and last name.

### Testing Methodology

Hypothesis is used to generate random string and None inputs.

The following tests are implemented:

- test_parse_booking_no_crash
- test_total_weight_no_crash
- test_tag_label_no_crash

### Bugs Identified

The original implementation produced:

- AttributeError for None inputs.
- IndexError for incomplete passenger names.

### Fixes Implemented

Input validation was added to all three functions.
Invalid inputs now raise controlled TypeError or ValueError
exceptions instead of unexpected runtime errors.

### Test Results

All three Hypothesis tests passed after fixing the
original implementation.

### Sample Execution

Booking Code: AI-203-12A
Total Baggage Weight: 42.5 kg
Passenger: Asha Rao
Generated Tag: A. RAO

### Requirements

Install dependencies using:

pip install -r requirements.txt

### Run Application

python airline_baggage.py

### Run Tests

python -m pytest test_airline_baggage.py -v

### Screenshots

See the screenshots folder for original execution,
failing tests, fixed execution and passing tests.
