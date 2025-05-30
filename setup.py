from setuptools import setup, find_packages
import pathlib

this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="python-nameof",
    version="1.2.1",
    description="A Python implementation of the C# nameof operator.",
    author="Alessio Lombardi",
    author_email="work@alelom.com",
    packages=find_packages(),
    py_modules=["nameof"],
    package_dir={"": "."},
    url="https://github.com/alelom/python-nameof",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
