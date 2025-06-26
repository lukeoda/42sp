from ex07.account import Account
import pytest
from ex07.utils import InsufficientBalance
from ex07.operation import Operation

def test_account_repr():
    ac = Account(1234, ['123.456.789-90'])
    assert repr(ac) == 'Account(1234, ...)'


def test_account_str():
    t = Account(1234, ['123.456.841-21'])
    print(str(t))
    assert str(t) == "Account: 1234 \nBalance: [+] R$ 0,00"

def test_account_withdraw():
    t = Account(1234, ['123.456.841-21'])
    t.deposit(123,'ATM deposit')
    t.withdraw(1,'ATM deposit')
    
    print(str(t))
    assert str(t) == "Account: 1234 \nBalance: [+] R$ 1,22"

def test_account_deposit():
    t = Account(1234, ['123.456.841-21'])
    t.deposit(123,'ATM deposit')
    
    print(str(t))
    assert str(t) == "Account: 1234 \nBalance: [+] R$ 1,23"

def test_account_deposit_value_0():
    t = Account(1234, ['123.456.841-21'])
    with pytest.raises(ValueError):
        t.deposit(0,'ATM deposit')


def test_account_withdraw_no_balance():
    t = Account(1234, ['123.456.841-21'])
    with pytest.raises(InsufficientBalance):
        t.withdraw(10,'ATM deposit')

def test_operation_str():
    t = Operation(1234, 'credit', 'ATM deposit')
    assert str(t) == '[+] R$ 12,34 (ATM deposit)'


def test_operation_repr():
    t = Operation(1234, 'credit', 'ATM deposit')
    assert repr(t) == "Operation(cents=1234, op_type='credit', description='ATM deposit')"



def test_operation_zero():
    try:
        Operation(0, 'credit', 'ATM deposit')
        assert False
    except ValueError:
        assert True
