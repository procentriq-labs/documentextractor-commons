from setuptools import setup, find_packages

setup(
    name="documentextractor_commons",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pydantic>=1.10.0",
    ],
)
