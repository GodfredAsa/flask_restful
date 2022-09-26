from test.pay import Pay


def test_name() -> None:
    fred = Pay("Fred", 100)
    assert fred.name == "Fred"


def test_deposit_invalid() -> None:
    fred = Pay("Fred", 100)
    fred.deposit(-5)
    assert fred.amount == 100


def test_deposit_valid() -> None:
    fred = Pay("Fred", 100)
    fred.deposit(50)
    assert fred.amount == 150


def test_withdraw_valid_amount() -> None:
    fred = Pay("Fred", 100)
    fred.withdrawal(50)
    assert fred.amount == 50


