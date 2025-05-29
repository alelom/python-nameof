# Python implementation of the C# nameof operator

python-nameof
=============

A Python utility that mimics the C# `nameof` operator, allowing you to get variable or attribute names as strings.

## Installation

```bash
pip install python-nameof
```

## Usage

```python
from nameof import nameof

foo = 123
print(nameof(foo))  # Output: 'foo'

class Bar:
    attr = 99
bar = Bar()
print(nameof("bar.attr"))  # Output: 'attr'
```

## License

MIT
