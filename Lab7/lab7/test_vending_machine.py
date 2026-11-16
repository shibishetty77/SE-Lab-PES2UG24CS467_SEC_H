import pytest
from hypothesis import given, strategies as st

from vending_machine import parse_coins, slot_position, change_due


# Test 1: parse_coins
@given(st.text() | st.none())
def test_parse_coins_no_unexpected_crash(s):
    try:
        result = parse_coins(s)
        assert isinstance(result, list)
        assert all(isinstance(c, int) and c > 0 for c in result)
    except ValueError:
        pass


def test_parse_coins_valid():
    assert parse_coins("5,10,25") == [5, 10, 25]


# Test 2: slot_position
@given(st.text() | st.none())
def test_slot_position_no_unexpected_crash(s):
    try:
        row, column = slot_position(s)
        assert row >= 0
        assert column >= 0
    except ValueError:
        pass


def test_slot_position_valid():
    assert slot_position("B7") == (1, 6)


# Test 3: change_due
@given(st.text() | st.none())
def test_change_due_no_unexpected_crash(s):
    try:
        result = change_due(s)
        assert isinstance(result, str)
        assert result.endswith(" five-coins")
    except ValueError:
        pass


def test_change_due_valid():
    assert change_due("200/150") == "10 five-coins"


# Invalid-input validation tests
@pytest.mark.parametrize("coins", [None, "", "1,,3", "hello", "0,5"])
def test_parse_coins_invalid(coins):
    with pytest.raises(ValueError):
        parse_coins(coins)


@pytest.mark.parametrize("code", [None, "", "A", "A0", "Axyz"])
def test_slot_position_invalid(code):
    with pytest.raises(ValueError):
        slot_position(code)


@pytest.mark.parametrize("payment", [None, "", "200", "abc/100", "100/200"])
def test_change_due_invalid(payment):
    with pytest.raises(ValueError):
        change_due(payment)
