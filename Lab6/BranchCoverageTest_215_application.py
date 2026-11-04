import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# Baggage fee tests

def test_unknown_cabin():
    with pytest.raises(ValueError):
        baggage_fee("first", 20, "domestic", False)


def test_negative_weight():
    with pytest.raises(ValueError):
        baggage_fee("economy", -5, "domestic", False)


def test_member_gets_extra_allowance():
    assert baggage_fee("economy", 25, "domestic", True) == 0


def test_member_exceeds_extra_allowance():
    assert baggage_fee("economy", 26, "domestic", True) == 20


def test_business_member():
    assert baggage_fee("business", 40, "domestic", True) == 0


def test_premium_member():
    assert baggage_fee("premium", 35, "domestic", True) == 0


def test_non_member():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_domestic_fee():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_domestic_high_excess():
    assert baggage_fee("economy", 36, "domestic", False) == 840


def test_international_high_excess():
    assert baggage_fee("economy", 36, "international", False) == 2100


def test_other_route():
    assert baggage_fee("economy", 20, "other", False) == 225


# Carry-on tests

def test_infant_allowed():
    assert carry_on_ok(5, 2, True) is True


def test_infant_not_allowed():
    assert carry_on_ok(5, 3, True) is False


def test_regular_passenger_weight_exceeded():
    assert carry_on_ok(8, 1, False) is False


def test_regular_passenger_weight_allowed():
    assert carry_on_ok(5, 1, False) is True


def test_regular_passenger_too_many_items():
    assert carry_on_ok(5, 2, False) is False


# Check-in tests

def test_open_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_late_with_baggage():
    assert check_in_status(50, True, False) == "late"


def test_closed_with_baggage():
    assert check_in_status(44, True, False) == "closed"


def test_open_without_baggage():
    assert check_in_status(45, False, False) == "open"


def test_late_without_baggage():
    assert check_in_status(35, False, False) == "late"


def test_closed_without_baggage():
    assert check_in_status(29, False, False) == "closed"


def test_international_checkin():
    assert check_in_status(105, False, True) == "open"


def test_international_checkin_late():
    assert check_in_status(95, False, True) == "late"


def test_international_checkin_closed():
    assert check_in_status(44, False, True) == "closed"
