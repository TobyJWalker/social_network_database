from lib.account import Account

def test_initalised_properly():
    acc = Account(1, "johndoe@gmail.com", "johndoe")

    assert acc.id == 1
    assert acc.email == 'johndoe@gmail.com'
    assert acc.username == 'johndoe'

def test_repr():
    acc = Account(1, "johndoe@gmail.com", "johndoe")

    assert str(acc) == "Account(1, johndoe@gmail.com, johndoe)"

def test_eq():
    acc_1 = Account(1, "johndoe@gmail.com", "johndoe")
    acc_2 = Account(1, "johndoe@gmail.com", "johndoe")

    assert acc_1 == acc_2