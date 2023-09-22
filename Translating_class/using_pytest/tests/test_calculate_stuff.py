from Translating_class.using_pytest import calculate_simply


def test_addition():
    assert calculate_simply.add_number(7, 3) == 10


def test_another_addition():
    assert calculate_simply.add_number(-7, -4) == -11
    