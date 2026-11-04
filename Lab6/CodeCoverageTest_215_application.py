import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# Baggage fee tests

def test_unknown_cabin():
    with pytest.raises(ValueError):
        baggage_fee("first", 20, "domestic", False)


def test_negative_weight():
    with pytest.raises(ValueError):
        baggage_fee("economy", -5, "domestic", False)


def test_member_premium_allowance():
    assert baggage_fee("premium", 35, "domestic", True) == 0


def test_business_member_allowance():
    assert baggage_fee("business", 40, "domestic", True) == 0


def test_within_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_domestic_baggage_fee():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_domestic_excess_above_20():
    assert baggage_fee("economy", 36, "domestic", False) == 840


def test_international_excess_above_20():
    assert baggage_fee("economy", 36, "international", False) == 2100


def test_other_route():
    assert baggage_fee("economy", 20, "other", False) == 225


# Carry-on baggage tests

def test_infant_allowed():
    assert carry_on_ok(5, 2, True) is True


def test_infant_exceeds_item_limit():
    assert carry_on_ok(5, 3, True) is False


def test_carry_on_weight_exceeded():
    assert carry_on_ok(8, 1, False) is False


def test_carry_on_allowed():
    assert carry_on_ok(5, 1, False) is True


def test_carry_on_item_limit_exceeded():
    assert carry_on_ok(5, 2, False) is False


# Check-in status tests

def test_checkin_open_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_checkin_late():
    assert check_in_status(50, True, False) == "late"


def test_checkin_closed():
    assert check_in_status(44, True, False) == "closed"


def test_international_checkin_open_without_baggage():
    assert check_in_status(105, False, True) == "open"
