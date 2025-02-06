# flasklaunch/setup.py

from setuptools import setup, find_packages

setup(
    name="flasklaunch",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "dynaconf",
        "pyyaml",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "flasklaunch = flasklaunch.cli:cli",
        ],
    },
)
