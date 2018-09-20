import unittest
import sportgraph.trello as trello
from datetime import date


class TestTrello(unittest.TestCase):
    def test_date_extraction(self):
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

    def test_extract_distance_from_string(self):
        comments = ['2,5 (some text) 20min',
                    '3 km, 1123 some text', '2,06', '2 more text']
        result = trello.extract_distance(comments)
        self.assertEqual(result[0], 2.5)
        self.assertEqual(result[1], 3)
        self.assertEqual(result[2], 2.06)
        self.assertEqual(result[3], 2)

    def test_extract_breaks(self):
        comments = ['5, 2 pausen',
                    '3 km, 1 pause dsfsd', '3,4, keine pause', '12 2 pausen more text']
        result = trello.extract_breaks(comments)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 2)
