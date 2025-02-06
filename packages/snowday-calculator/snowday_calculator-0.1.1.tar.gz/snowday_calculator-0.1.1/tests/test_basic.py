import datetime
import unittest
from unittest.mock import MagicMock, patch

from snowday_calculator import (
    Prediction,
    SchoolType,
    datetime_to_daycode,
    predict,
)


class TestSnowdayCalculator(unittest.TestCase):
    def test_datetime_to_daycode(self):
        """Test conversion of datetime to daycode string."""
        day = datetime.datetime(2025, 2, 5)
        self.assertEqual(datetime_to_daycode(day), "20250205")

    def test_prediction_set_and_get(self):
        """Test that setting and getting a prediction works correctly."""
        pred = Prediction()
        daycode = datetime_to_daycode(datetime.datetime.today())
        pred._set_data(daycode, 85)
        self.assertEqual(pred.chance(datetime.datetime.today()), 85)

    def test_chance_today_and_tmrw(self):
        """Test chance_today and chance_tmrw methods of Prediction."""
        pred = Prediction()
        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(days=1)

        # Manually set chances for today and tomorrow
        daycode_today = datetime_to_daycode(today)
        daycode_tmrw = datetime_to_daycode(tomorrow)
        pred._set_data(daycode_today, 50)
        pred._set_data(daycode_tmrw, 60)

        self.assertEqual(pred.chance_today(), 50)
        self.assertEqual(pred.chance_tmrw(), 60)

    @patch("snowday_calculator.requests.get")
    def test_predict(self, mock_get):
        """
        Test the predict function.

        This test patches requests.get to return a dummy response containing
        two predictions. It then verifies that the predict function correctly
        parses the response and sets the prediction values.
        """
        # Create a dummy response text that simulates the JavaScript output.
        dummy_response_text = "theChance[20250205] = 85.0; theChance[20250206] = 90.0;"

        # Configure the mock to return an object with .text attribute.
        mock_response = MagicMock()
        mock_response.text = dummy_response_text
        mock_get.return_value = mock_response

        # Call the predict function.
        result = predict("12345", snowdays=2, schooltype=SchoolType.PUBLIC)

        # Verify that the predictions are parsed correctly.
        # Note: Since our dummy daycodes are static strings, we create datetime
        # objects that would produce those daycodes.
        day1 = datetime.datetime.strptime("20250205", "%Y%m%d")
        day2 = datetime.datetime.strptime("20250206", "%Y%m%d")

        self.assertEqual(result.chance(day1), 85.0)
        self.assertEqual(result.chance(day2), 90.0)

        # Optionally, verify that requests.get was called with expected parameters.
        mock_get.assert_called_with(
            "https://www.snowdaycalculator.com/prediction.php",
            params={"zipcode": "12345", "snowdays": 2, "extra": SchoolType.PUBLIC},
        )


if __name__ == "__main__":
    unittest.main()
