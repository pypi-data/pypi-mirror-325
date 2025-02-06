![Read the Docs](https://img.shields.io/readthedocs/snowday-calculator)
![Codecov](https://img.shields.io/codecov/c/github/danielkorkin/snowday-calculator)
![PyPI - Version](https://img.shields.io/pypi/v/snowday-calculator)

# snowday-calculator

A Python package to predict the chance of a snow day based on zipcode, snow days, and school type.

## Installation

```bash
pip install snowday-calculator
```

## Usage

```python
from snowday_calculator import predict, SchoolType

# Example: Predict the chance for zipcode "12345"
result = predict("12345", snowdays=2, schooltype=SchoolType.PUBLIC)
print("Chance today:", result.chance_today())
print("Chance tomorrow:", result.chance_tmrw())
```

## Links

-   [Documentation](https://snowday-calculator.readthedocs.io/)
-   [Code Coverage](https://codecov.io/gh/danielkorkin/snowday-calculator)
-   [PyPI](https://pypi.org/project/snowday-calculator/)
