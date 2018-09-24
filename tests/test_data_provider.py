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

    def test_normalize_breaks(self):
        breaks = [2, 3, 0, 2, 1, 4]
        result = data_provider.normalize_breaks(breaks)
        self.assertAlmostEqual(result[0], 0.4, places=2)
        self.assertAlmostEqual(result[1], 0.6, places=2)
        self.assertAlmostEqual(result[2], 0, places=2)
        self.assertAlmostEqual(result[3], 0.4, places=2)
        self.assertAlmostEqual(result[4], 0.2, places=2)
        self.assertAlmostEqual(result[5], 0.8, places=2)
