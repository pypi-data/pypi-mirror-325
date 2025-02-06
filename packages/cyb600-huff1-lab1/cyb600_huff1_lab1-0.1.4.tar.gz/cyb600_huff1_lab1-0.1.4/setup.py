from setuptools import setup, find_packages

setup(
    name="cyb600_huff1_lab1",
    version="0.1.4",
    author="Darnell Huff",
    author_email="huff4@canisius.edu",
    description="This package creates a webserver that will spit out the current time",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dhuffCanisius/CYB600_Lab1",
    packages=find_packages(),
    python_requires=">=3.6",
)

