from setuptools import setup, find_packages

setup(
    name="nuse",
    version="0.1.0",
    author='Jacob Molin Nielsen',
    author_email='jacob.molin@me.com',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "nuse = nuse.nuse:main",
        ],
    },
)