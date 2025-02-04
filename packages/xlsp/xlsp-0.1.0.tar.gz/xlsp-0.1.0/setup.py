from setuptools import setup, find_packages

setup(
    name="xlsp",
    version="0.1.0",
    author="Steven P. Davis",
    author_email="sdavis@davisportal.com",
    description="A Python library for interacting with Excel files on SharePoint.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sdavis9248/xlsp",  # Update with your repo
    packages=find_packages(),
    install_requires=[
        "requests",
        "openpyxl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

