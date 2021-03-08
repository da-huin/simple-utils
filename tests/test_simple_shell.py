import simple_utils

def test_dynamic_check_output():
    assert simple_utils.shell.dynamic_check_output('cat assets/message.txt') == 'Hello World'

