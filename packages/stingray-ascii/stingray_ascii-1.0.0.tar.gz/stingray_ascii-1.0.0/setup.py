# setup.py

import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="stingray-ascii",
    version="1.0.0", ##
    author="Stingray Park",
    author_email="someone@example.com", ##
    description="A useless library that helps you print stingray ASCII arts.", ##
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stingraypark/stingray-ascii", ##
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    "typing>=3.5.0",
    ],
)