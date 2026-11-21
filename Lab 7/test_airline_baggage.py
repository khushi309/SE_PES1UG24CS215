from hypothesis import given, strategies as st
from airline_baggage import parse_booking, total_weight, tag_label


@given(st.text() | st.none())
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except (TypeError, ValueError):
        pass


@given(st.text() | st.none())
def test_total_weight_no_crash(s):
    try:
        total_weight(s)
    except (TypeError, ValueError):
        pass


@given(st.text() | st.none())
def test_tag_label_no_crash(s):
    try:
        tag_label(s)
    except (TypeError, ValueError):
        pass
