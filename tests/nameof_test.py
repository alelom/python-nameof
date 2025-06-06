if True:
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    os.environ["nameof_test"] = "True"
    
from nameof import nameof
import sys


def test_variable_name():
    foo = 123
    assert nameof(foo) == "foo"


def test_multiple_variables_same_value():
    a = b = 42 # type: ignore
    result_a = nameof(a)
    result_b = nameof(b)
    
    assert result_a == "a", "Only the first variable name should be returned"
    assert result_b == "b", "Only the first variable name should be returned"


def test_invalid_arg_int():
    try:
        nameof(42)
    except ValueError:
        return
    
    raise Exception("Expected ValueError not raised for unknown variable name.")


def test_invalid_arg_str():
    try:
        nameof("asd.bar")
    except ValueError:
        pass
    
    try:
        nameof("nameof(bar)")
    except ValueError:
        return
    
    raise Exception("Expected ValueError not raised for unknown variable name.")


def test_function_param():
    def f(x: int):
        return nameof(x)

    assert f(5) == "x"
    
    
def test_string_interpolation():
    def f(x: int):
        return nameof(x)

    assert f"{f(5)} and {f(10)}" ==  "x and x"


def test_class_variable():
    class MyClass:
        class_var = "abc"
    name = nameof(MyClass.class_var)
    assert name == "class_var"


def test_instance_variable():
    class MyClass:
        def __init__(self):
            self.instance_var = 123
    obj = MyClass()
    name = nameof(obj.instance_var) 
    assert name == "instance_var"


def test_nested_class_property():
    class Inner:
        @property
        def value(self):
            return 10

    class Outer:
        def __init__(self):
            self.inner = Inner()

    outer = Outer()
    
    # Test nameof on property of another class via instance
    assert nameof(outer.inner.value) == "value", f"Returned: {nameof(outer.inner.value)} instead of 'value'"
    

def test_multiple_names():
    x=1
    y=1
    
    try:
        name = nameof(1)
    except ValueError:
        return
    
    raise Exception("Expected ValueError not raised for unknown variable name.")
    
    
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


