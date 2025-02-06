import unittest
from datetime import datetime
from snowday_calculator import datetime_to_daycode, Prediction


class TestSnowdayCalculator(unittest.TestCase):
    def test_datetime_to_daycode(self):
        day = datetime(2025, 2, 5)
        self.assertEqual(datetime_to_daycode(day), "20250205")

    def test_prediction_set_and_get(self):
        pred = Prediction()
        daycode = datetime_to_daycode(datetime.today())
        pred._set_data(daycode, 85)
        self.assertEqual(pred.chance(datetime.today()), 85)


if __name__ == "__main__":
    unittest.main()
