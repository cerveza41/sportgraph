import unittest
from datetime import date
import sportgraph.data_provider as data_provider


class TestDataProvider(unittest.TestCase):
    def test_first_date_is_considered_in_calculation(self):
        dates = [
            date(2017, 12, 19),
            date(2017, 12, 28)
        ]
        result = data_provider.calculate_days_in_between(dates)
        self.assertEqual(result, [0, 9])
