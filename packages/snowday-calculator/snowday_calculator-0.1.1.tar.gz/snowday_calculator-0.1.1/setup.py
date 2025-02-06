import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snowday-calculator",
    version="0.1.1",
    author="Daniel Korkin",
    author_email="daniel.d.korkin@gmail.com",
    description="A package for calculating snow day predictions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielkorkin/snowday-calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",  # Required dependency
    ],
    extras_require={
        "dev": [
            "sphinx",
            "sphinx-rtd-theme",
            "sphinx-autodoc-typehints",
            "pytest",
            "pytest-cov",  # Added for test coverage
            "coverage",  # Added for generating coverage reports
            "pre-commit",
            "ruff",
            "black",
            "yamlfmt",  # For auto-formatting YAML files
            "doc8",  # For linting RST files in docs
        ]
    },
)
