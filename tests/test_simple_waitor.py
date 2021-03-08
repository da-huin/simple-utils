import simple_utils

def test_waitor():
    waiter = simple_utils.waitor.Waiter(items=['1','2','3','4','5'])
    assert waiter.get() == '1'
    waiter.put('6')
    assert [waiter.get() for i in range(5)] == ['2', '3', '4', '5', '6']
