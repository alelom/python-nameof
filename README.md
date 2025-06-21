# `python_nameof`: a Python implementation of C# `nameof` operator

> _This is a follow-up to [this project](https://github.com/alexmojaki/nameof) since the author archived it, preferring the [`varname`](https://github.com/pwwang/python-varname) library which [used to cover `nameof`](https://github.com/pwwang/python-varname/issues/117), but then [`varname` deprecated it](https://github.com/pwwang/python-varname/commit/1a342b3dc54f0363deb26a80dcdf608341a9594c#diff-dc2f15ddf68ad966f2e3d02f7f4e307cf691fed747df8087c10c3861e2bbc031)._

> NOTE: [`nameof()` is now back in v.0.15.0 of `varname`](https://github.com/pwwang/python-varname/issues/117#issuecomment-2992408664).

A Python utility that mimics the [C# `nameof` operator](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/nameof?redirectedfrom=MSDN), allowing you to get variable, attribute, or property names as strings at runtime.

It is an essential operator to allow flexible and reliable refactoring, among [many other things](https://stackoverflow.com/q/31695900/3873799).

This implementation supports string interpolation, so it's easy to reference variable names when logging, e.g.  
`log.error(f"{nameof(somevariable)} is incorrect")`.

## Installation

Pip:

```bash
pip install python_nameof
```

My recommendation is to always use [`uv`](https://docs.astral.sh/uv/) instead of pip – I personally think it's the best package and environment manager for Python.

```bash
uv add python_nameof
```

## Usage

Import:
```python
from nameof import nameof
```

Simple usage:

```python
foo = 123
nameof(foo)  # Output: 'foo'
```

You can test it in a simple refactoring operation. For example:

```python
def print_variables(temperature: int)
    print(f"The parameter {nameof(temperature)} is: {temperature}")
```

> The parameter temperature is: 34

If you refactor (_e.g. VSCode: press **F2** on the variable name_) the input parameter from `temperature` to `temperature_celsius`, you will get:
```python
def print_variables(temperature_celsius: int)
    print(f"The parameter {nameof(temperature_celsius)} is: {temperature_celsius}")
```

So the _printed name follows the name of the actual parameter after a refactor_.

> The parameter temperature_celsius is: 34



### Additional Parameters

The `nameof` function supports two optional parameters for formatting the output:

- `wrap_in_chars`: Wraps the variable name with the specified string at the start and end.
- `replace_with_whitespace`: Removes all occurrences of the specified character(s) from the variable name and replaces them with a whitespace. Accepts a string or a list of strings.

These are especially useful if you are logging to markdown format (printing messages as Markdown), to format variable names as code or to remove underscores for readability.


```python
some_param = 1

# Combine both: wrap in backticks and remove underscores
nameof(some_param, "`", "_")  # Output: '`some param`'

```

This is useful when generating Markdown documentation or error messages:

```python
def print_variables(temperature_celsius: int)
    print(f"The parameter {nameof(temperature_celsius, "`", "_")} is: {temperature_celsius}")
```

This will plot a nicely formatted markdown, useful if you do logging in markdown:
> The parameter `temperature celsius` is: 34


### Multiple assignments

If a variable is assigned twice, only the first name is returned.

```python
a = b = 1

nameof(a) # returns "a"
nameof(b) # returns "b"

nameof(1) # raises ValueError (see next section below)
```

### Error Handling

If you pass a value or an expression that is not a variable or attribute, `nameof` raises a `ValueError`:

```python
nameof(42)            # Raises ValueError
nameof("foo.bar")     # Raises ValueError
nameof("nameof(bar)") # Raises ValueError
```


## More usage examples

`nameof()` supports string interpolation, so it's easier to reference variable names when logging,
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
nameof(Bar.attr)      # Output: 'attr'
nameof(bar.attr)      # Output: 'attr'
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
nameof(outer.inner.value)  # Output: 'value'
```


