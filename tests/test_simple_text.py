import simple_utils

def test_get_random_string():
    assert simple_utils.text.get_random_string(10) != simple_utils.text.get_random_string(10)

def test_set_var():
    assert simple_utils.text.set_var("""my name is {{name}}""", {'name': 'jaden'}) == 'my name is jaden'

def test_get_var():
    assert simple_utils.text.get_var("""my name is {{name}}, and {{hello}}""") == ['{{name}}', '{{hello}}']

def test_is_unchanged_var_exists():
    assert simple_utils.text.is_unchanged_var_exists('my name is {{name}}') == True
    assert simple_utils.text.is_unchanged_var_exists('my name is jaden') == False
