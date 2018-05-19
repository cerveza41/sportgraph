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

    return (calculate_days_in_between(d), [1.85, 1.90, 2.00, 2.5, 2.06, 2.26, 2.48, 2.08, 2.6,
                                           2.77, 2.48, 2.90, 1.47, 2.80, 2.24, 3.0, 2.67, 3, 3.22, 3.3])
