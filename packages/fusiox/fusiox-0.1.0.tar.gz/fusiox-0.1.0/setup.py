from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fusiox",  # Nama unik untuk package Anda di PyPI
    version="0.1.0",
    author="Alex Sirait",
    author_email="alexsirait1001@gmail.com",
    description="This super package is called fusiox.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexsirait/fusiox",  # Ganti dengan repo Anda
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.2',
)
