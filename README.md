# `python-nameof`: a Python implementation of C# `nameof` operator

A Python utility that mimics the [C# `nameof` operator](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/nameof?redirectedfrom=MSDN), allowing you to get variable, attribute, or property names as strings at runtime.

It is an essential operator to allow flexible and reliable refactoring, among [many other things](https://stackoverflow.com/q/31695900/3873799).

This implementation supports string interpolation, so it's easy to reference variable names when logging, e.g.  
`log.error(f"{nameof(somevariable)} is incorrect")`.

_**NOTE**: This is a follow up to [this project](https://github.com/alexmojaki/nameof) since the author archived it, preferring the [`varname`](https://github.com/pwwang/python-varname) library which [used to cover `nameof`](https://github.com/pwwang/python-varname/issues/117), but [varname has deprecated it](https://github.com/pwwang/python-varname/commit/1a342b3dc54f0363deb26a80dcdf608341a9594c#diff-dc2f15ddf68ad966f2e3d02f7f4e307cf691fed747df8087c10c3861e2bbc031)._

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
def myFuncWithAmazingLogging(first_param: int):
    valid_threshold = 10
    if first_param < 10:
        print(f"The parameter {nameof(first_param)} should be less than {valid_threshold}")
```

It works for class attributes and instance variables.

```python
class Bar:
    attr = 99
bar = Bar()
print(nameof(Bar.attr))      # Output: 'attr'
print(nameof(bar.attr))      # Output: 'attr'
```

It works also for nested classes.

```python
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

## Multiple assignments

If a variable is assigned twice, only the first name is returned.

```python
a = b = 1

nameof(a) # returns "a"
nameof(b) # returns "b"

nameof(1) # raises ValueError (see next section below)
```

## Error Handling

If you pass a value or an expression that is not a variable or attribute, `nameof` raises a `ValueError`:

```python
nameof(42)            # Raises ValueError
nameof("foo.bar")     # Raises ValueError
nameof("nameof(bar)") # Raises ValueError
```
