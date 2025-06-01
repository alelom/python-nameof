if True:
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    os.environ["nameof_test"] = "True"
    
from nameof import nameof
import pytest

def test_wrap_in_chars():
    my_var = 123
    assert nameof(my_var, wrap_in_chars='"') == '"my_var"'
    assert nameof(my_var, wrap_in_chars='*') == '*my_var*'
    assert nameof(my_var, wrap_in_chars='[]') == '[]my_var[]'
    assert nameof(my_var, wrap_in_chars='`') == '`my_var`'

def test_replace_with_whitespace_str():
    my_var = 123
    assert nameof(my_var, replace_with_whitespace='_') == 'my var'
    assert nameof(my_var, replace_with_whitespace='a') == 'my_v r'
    assert nameof(my_var, replace_with_whitespace='m') == ' y_var'

def test_replace_with_whitespace_list():
    my_var = 123
    assert nameof(my_var, replace_with_whitespace=['_']) == 'my var'
    assert nameof(my_var, replace_with_whitespace=['a', 'v']) == 'my_  r'

def test_wrap_and_remove():
    my_var = 123
    assert nameof(my_var, wrap_in_chars='`', replace_with_whitespace='_') == '`my var`'
    assert nameof(my_var, '`', '_') == '`my var`'
    assert nameof(my_var, wrap_in_chars='"', replace_with_whitespace='a') == '"my_v r"'

def test_attribute_access():
    class Dummy:
        attr_name = 1
    d = Dummy()
    assert nameof(d.attr_name, replace_with_whitespace='_') == 'attr name'
    assert nameof(d.attr_name, wrap_in_chars='`', replace_with_whitespace='_') == '`attr name`'
    assert nameof(d.attr_name, replace_with_whitespace='*') == 'attr_name'
    assert nameof(d.attr_name, replace_with_whitespace='a') == ' ttr_n me'
    assert nameof(d.attr_name, wrap_in_chars='`', replace_with_whitespace=['a', '_']) == "` ttr n me`"
    
    
def run_all_tests():
    current_module = sys.modules[__name__]
    test_functions = [
        getattr(current_module, name)
        for name in dir(current_module)
        if name.startswith("test_") and callable(getattr(current_module, name))
    ]
    for test_func in test_functions:
        test_func()
        
    print("All tests passed.")


if __name__ == "__main__":
    run_all_tests()