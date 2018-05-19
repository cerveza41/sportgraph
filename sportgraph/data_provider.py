from datetime import date
from typing import List, Tuple
import sportgraph.trello as trello


def calculate_days_in_between(dates: List[date]) -> List[int]:
    lowest_date = min(dates)
    diffs_to_lowest_date = []
    for d in dates:
        diffs_to_lowest_date.append((d-lowest_date).days)
    return diffs_to_lowest_date


def get_axis_values() -> Tuple[List[int], List[float]]:
    dates, comments = trello.request_all_comments()
    d = trello.extract_dates(dates)
    distance = trello.extract_distance(comments)

    return (calculate_days_in_between(d), distance)
