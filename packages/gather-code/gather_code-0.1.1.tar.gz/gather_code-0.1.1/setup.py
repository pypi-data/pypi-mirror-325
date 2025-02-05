# setup.py
from setuptools import setup, find_packages

setup(
    name="gather_code",
    version="0.1.1",
    description="A tool to gather your codebase into a single file with a directory tree and file contents.",
    author="Oleksii Furman",
    author_email="qizzup@gmail.com",
    url="https://github.com/ofurman/gather_code",  # update as needed
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gather-code=gather_code.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or your license
        "Operating System :: OS Independent",
    ],
)
