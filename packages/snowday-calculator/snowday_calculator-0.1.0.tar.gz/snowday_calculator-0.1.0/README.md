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
