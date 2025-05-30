# Release Process

Update the version in `setup.py`.

Then build as below.

Requirement: `pip install build`

## Build from Windows

```cmd
del dist\*.* /Q && python -m build
```

to delete any previous releases from the `dist` folder and then build.

## Build from Linux

```bash
rm dist/*.* | python3 -m build
```

to delete any previous releases from the `dist` folder and then build.


## Release on PyPI

   
Upload to PyPi: 

```cmd/bash
python -m twine upload dist/*
```

Upload to PyPiTest: 

```cmd/bash
python -m twine upload --repository testpypi dist/*
```
