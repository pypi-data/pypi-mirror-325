"""
snowday_calculator package.

This module provides functions and classes to predict the chance of a snow day
based on zipcode, snow days, and school type.
"""

import datetime
import re

import requests


class SchoolType:
    """Constants representing different school types for prediction calculations."""

    PUBLIC = 0
    URBAN_PUBLIC = 0.4
    RURAL_PUBLIC = -0.4
    PRIVATE = -0.4
    BOARDING = 1


def datetime_to_daycode(day: datetime.datetime) -> str:
    """Convert a datetime object to a daycode string in the format YYYYMMDD.

    Args:
        day (datetime.datetime): The datetime object to convert.

    Returns:
        str: The daycode in the format "YYYYMMDD".
    """
    return "{0:%Y%m%d}".format(day)


class Prediction:
    """Class to hold and retrieve snow day prediction chances."""

    def __init__(self):
        """Initialize an empty prediction dictionary."""
        self.data = {}

    def _set_data(self, daycode: str, chance: float) -> None:
        """Set the chance for a given day code, capping the chance at 99.

        Args:
            daycode (str): The daycode string.
            chance (float): The chance value to record.
        """
        self.data[daycode] = min(99, float(chance))

    def chance(self, day: datetime.datetime):
        """Retrieve the prediction chance for a specified day.

        Args:
            day (datetime.datetime): The day for which to retrieve the chance.

        Returns:
            float or None: The chance value if available; otherwise, None.
        """
        daycode = datetime_to_daycode(day)
        return self.data.get(daycode)

    def chance_today(self):
        """Retrieve the prediction chance for today.

        Returns:
            float or None: Today's chance value if available; otherwise, None.
        """
        return self.chance(datetime.datetime.today())

    def chance_tmrw(self):
        """Retrieve the prediction chance for tomorrow.

        Returns:
            float or None: Tomorrow's chance value if available; otherwise, None.
        """
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        return self.chance(tomorrow)


def predict(zipcode: str, snowdays: int = 0, schooltype: int = SchoolType.PUBLIC) -> Prediction:
    """Predict the chance of a snow day.

    Makes an HTTP request to the snow day prediction service and parses the
    JavaScript response to extract prediction chances.

    Args:
        zipcode (str): The zipcode for which to predict.
        snowdays (int, optional): Number of snow days to consider. Defaults to 0.
        schooltype (int, optional): School type constant from SchoolType. Defaults to SchoolType.PUBLIC.

    Returns:
        Prediction: An instance of Prediction containing the parsed chances.
    """
    response = requests.get(
        "https://www.snowdaycalculator.com/prediction.php",
        params={"zipcode": zipcode, "snowdays": snowdays, "extra": schooltype},
    ).text

    js_predictions = re.findall(r"theChance\[\d+\] = [\d\.]+;", response)
    result = Prediction()

    for pred in js_predictions:
        key, value = pred.split(" = ")
        daycode = re.findall(r"\d+", key)[0]
        chance = re.findall(r"[\d\.]+", value)[0]
        result._set_data(daycode, chance)

    return result
