from .operation import Operation

def test_operation_str():
    t = Operation(1234, 'credit', 'ATM deposit')
    assert str(t) == '[+] R$ 12,34 (ATM deposit)'


def test_operation_repr():
    t = Operation(1234, 'credit', 'ATM deposit')
    assert repr(t) == "Operation(cents=1234, op_type='credit', description='ATM deposit')"



def test_operation_zero():
    try:
        t = Operation(0, 'credit', 'ATM deposit')
        assert False
    except ValueError:
        assert True