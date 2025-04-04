from setuptools import setup, find_packages

setup(
    name="nbipackager",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "configparser>=5.0.0",
    ],
    entry_points={
        "console_scripts": [
            "packager=nbipackager.cli:main",
        ],
    },
)
