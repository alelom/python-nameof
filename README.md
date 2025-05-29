# Python implementation of the C# nameof operator

python-nameof
=============

A Python utility that mimics the C# `nameof` operator, allowing you to get variable, attribute, or property names as strings at runtime.

It supports string interpolation, so it's easier to reference variable names when logging, allowing for easier and more robust refactoring.

## Installation

Pip:

```bash
pip install python-nameof
```

My recommendation is to always use [`uv`](https://docs.astral.sh/uv/) instead of pip – I personally think it's the best package and environment manager for Python.

```bash
uv add python-nameof
```

## Usage

Import:
```python
from nameof import nameof
```

Simple usage:

```python
foo = 123
print(nameof(foo))  # Output: 'foo'
```

It supports string interpolation, so it's easier to reference variable names when logging,
allowing for easier refactoring.  
In the example below, refactoring the name of second_param will propagate to the printed message without having to manually do it.

```python
def myFuncWithAmazingLogging(first_param: int, second_param: int):
    valid_threshold = 10
    if second_param < 10:
        print(f"The parameter {nameof(second_param)} should be less than {valid_threshold}")
```

It works for class attributes and instance variables.

```python
class Bar:
    attr = 99
bar = Bar()
print(nameof(Bar.attr))      # Output: 'attr'
print(nameof(bar.attr))      # Output: 'attr'

class MyClass:
    def __init__(self):
        self.instance_var = 123

obj = MyClass()
print(nameof(obj.instance_var))  # Output: 'instance_var'

class Inner:
    @property
    def value(self):
        return 10

class Outer:
    def __init__(self):
        self.inner = Inner()

outer = Outer()
print(nameof(outer.inner.value))  # Output: 'value'
```

## Error Handling

If you pass a value or an expression that is not a variable or attribute, `nameof` raises a `ValueError`:

```python
nameof(42)            # Raises ValueError
nameof("foo.bar")     # Raises ValueError
nameof("nameof(bar)") # Raises ValueError
```
