import pytest
from homeworks import summ_numbers

#test1
@pytest.mark.parametrize("input_str,expected", [
    ('1,2,3,4,5', 15),
    ('1,2,3,4,23', 33),
    ('1,25,3,43,5', 77),
])
def test_summ_numbers_valid_numbers(input_str, expected):
    assert summ_numbers(input_str) == expected

@pytest.mark.parametrize("input_str", [
    'werty5',
    '1,2,3,4,e',
    '1,25,3,43.5',
    '',
    ' g, ,5, ',
    '1,,2',
    '1,,,3'
])
def test_summ_numbers_negative(input_str):
    assert summ_numbers(input_str) == "Не можу це зробити"

@pytest.mark.parametrize("input_str,expected", [
    ('42', 42),
    (' 1 , 2 , 3 ', 6)
])
def test_summ_numbers_edge_cases(input_str, expected):
    assert summ_numbers(input_str) == expected

from homeworks import pair_sum
#test2

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 345, 348),
    (45, 1, 46),
    (0, 23, 23),
    (3, -345, -342),
    (0, 0, 0),
    (2.45, 3, 5.45),
    (0, -5, -5),
    (1_000_000, 2_342_324, 3_342_324)
])
def test_pair_sum(num1, num2, expected):
    assert pair_sum(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected_exception", [
    (3, "a", TypeError),
    (None, 23, TypeError),
    ([1, 2], 0, TypeError),
    ({"s": 3}, 3, TypeError),
    (True, "fgfh4", TypeError)
])
def test_pair_sum_negative(num1, num2, expected_exception):
    with pytest.raises(expected_exception):
        pair_sum(num1, num2)

from homeworks import multiplication_table
#test3

@pytest.mark.parametrize("number,expected", [
    (1, ['1x1=1', '1x2=2', '1x3=3', '1x4=4', '1x5=5', '1x6=6', '1x7=7', '1x8=8', '1x9=9', '1x10=10', '1x11=11', '1x12=12', '1x13=13', '1x14=14', '1x15=15', '1x16=16', '1x17=17', '1x18=18', '1x19=19', '1x20=20', '1x21=21', '1x22=22', '1x23=23', '1x24=24', '1x25=25']),
    (5, ['5x1=5', '5x2=10', '5x3=15', '5x4=20', '5x5=25']),
    (" 10 ", ['10x1=10', '10x2=20']),
    (26, []),
    (-5, ['-5x1=-5', '-5x2=-10', '-5x3=-15', '-5x4=-20', '-5x5=-25'])
])
def test_valid_numbers(number, expected):
    assert multiplication_table(number) == expected

def test_zero_raises():
    with pytest.raises(ValueError, match="Функція не приймає 0"):
        multiplication_table(0)

@pytest.mark.parametrize("bad_input", ["abc", "", "  ", "5a", "7.5", "1,2"])
def test_invalid_input(bad_input):
    with pytest.raises(ValueError, match="Функція приймає лише цілі числа"):
        multiplication_table(bad_input)