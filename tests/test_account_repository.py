from lib.account_repository import *

def test_all_accounts(db_connection):
    db_connection.seed('seeds/social_network.sql')
    acc_repo = AccountRepository(db_connection)

    accounts = acc_repo.all()

    assert len(accounts) == 3
    assert accounts[0].id == 1
    assert accounts[0].username == 'johnsmith'
    assert accounts[-1].id == 3
    assert accounts[-1].username == 'katemoor'

def test_find_account(db_connection):
    db_connection.seed('seeds/social_network.sql')
    acc_repo = AccountRepository(db_connection)

    account = acc_repo.find(1)

    assert account.id == 1
    assert account.username == 'johnsmith'
    assert account.email == 'johnsmith@gmail.com'