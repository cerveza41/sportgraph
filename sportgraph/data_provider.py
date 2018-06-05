from datetime import date
from typing import List, Tuple
import sportgraph.trello as trello


def calculate_days_in_between(dates: List[date]) -> List[int]:
    lowest_date = min(dates)
    diffs_to_lowest_date = []
    for d in dates:
        diffs_to_lowest_date.append((d-lowest_date).days)
    return diffs_to_lowest_date


class DataProvider():
    def __init__(self):
        raw_dates, comments = trello.request_all_comments()
        self.dates = calculate_days_in_between(trello.extract_dates(raw_dates))
        self.distances = trello.extract_distance(comments)
