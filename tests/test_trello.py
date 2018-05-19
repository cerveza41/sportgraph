import unittest
import sportgraph.trello as trello
from datetime import date


class TestTrello(unittest.TestCase):
    def test_date_transformation(self):
        dates = ['2018-01-22T19:38:56.244Z', '2018-05-16T16:02:03.535Z']
        result = trello.extract_dates(dates)
        self.assertEqual(result[0], date(2018, 1, 22))
        self.assertEqual(result[1], date(2018, 5, 16))

    def test_dates_list_is_ascending(self):
        dates = ['2018-01-22T19:38:56.244Z',
                 '2018-05-16T16:02:03.535Z', '2018-01-20T19:38:56.244Z']
        result = trello.extract_dates(dates)
        self.assertEqual(result[0], date(2018, 1, 20))
        self.assertEqual(result[1], date(2018, 1, 22))
        self.assertEqual(result[2], date(2018, 5, 16))
