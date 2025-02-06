from setuptools import setup, find_packages

setup(
    name="flasklaunch",
    version="0.1.2",
    author="Leonan Thomaz",
    author_email="leonan.thomaz@gmail.com",
    description="A tool to quickly launch Flask projects",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/leonanthomaz/flasklaunch",
    license="MIT",
    keywords=["flask", "web", "development", "cli", "scaffolding", "bootstrap", "api", "restful", "database", "sqlalchemy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "flask",
        "dynaconf",
        "pyyaml",
        "click",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "flasklaunch = flasklaunch.cli:cli",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/leonanthomaz/flasklaunch/issues",
        "Documentation": "https://github.com/leonanthomaz/flasklaunch/wiki",
        "Source Code": "https://github.com/leonanthomaz/flasklaunch",
    },
    tests_require=["pytest"],
    test_suite="pytest",
    extras_require={
        "dev": ["flake8", "black"],
    },
)