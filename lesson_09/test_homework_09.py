import pytest
from homeworks import summ_numbers, multiplication_table

def test_valid_numbers():
    assert summ_numbers('1,2,3,4,5') == 15
    assert summ_numbers('1,2,3,4,23') == 33
    assert summ_numbers('1,25,3,43,5') == 77

def test_invalid_values():
    assert summ_numbers('werty5') == "Не можу це зробити"
    assert summ_numbers('1,2,3,4,e') == "Не можу це зробити"
    assert summ_numbers('1,25,3,43.5') == "Не можу це зробити"

def test_empty_string():
    assert summ_numbers('') == "Не можу це зробити"

def test_only_spaces():
    assert summ_numbers(' g, ,5, ') == "Не можу це зробити"

from homeworks import pair_sum

def test_different_numbers():
    assert pair_sum(3,345) == 348
    assert pair_sum(45,1) == 46
    assert pair_sum(0,23) == 23

def test_numbers_negative():
    assert pair_sum(3, -345) == -342
    assert pair_sum(0, 0) == 0
    assert pair_sum(2.45,3) == 5.45




