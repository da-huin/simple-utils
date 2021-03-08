import simple_utils

def test_web():
    assert simple_utils.web.python_vars_to_javascript({
        'hello': 'world',
        'abc': 'def'
    }, without_script_tag=True).find('var abc =') != -1