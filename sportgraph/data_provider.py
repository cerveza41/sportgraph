from datetime import date
from typing import List, Tuple
import sportgraph.trello as trello


def calculate_days_in_between(dates: List[date]) -> List[int]:
    lowest_date = min(dates)
    return [(date-lowest_date).days for date in dates]


def normalize_breaks(breaks_list: List[int]) -> List[float]:
    """ returns normalized trend based on number of breaks
        from no_breaks to many_breaks (0..1)
    """
    max_breaks = max(breaks_list) + 1
    return [breaks/max_breaks for breaks in breaks_list]


def moving_average(numbers: List[float]) -> List[float]:
    """ returns the moving average of the input
        the returned list has same dimension as the input
    """
    # previous n data to be considered
    N = 3
    cumulative_sum = [0]
    moving_aves = []

    for i, value in enumerate(numbers, 1):
        cumulative_sum.append(cumulative_sum[i-1] + value)
        if i >= N:
            # calc average of latest N sums
            moving_ave = (cumulative_sum[i] - cumulative_sum[i-N])/N
            moving_aves.append(moving_ave)

    # fill up result list to have same dimension as input
    while len(moving_aves) < len(numbers):
        moving_aves.insert(0, moving_aves[0])

    return moving_aves


class DataProvider():
    def __init__(self):
        raw_dates, comments = trello.request_all_comments()
        self.dates = calculate_days_in_between(trello.extract_dates(raw_dates))
        self.distances = trello.extract_distance(comments)
        self.trend = moving_average(
            normalize_breaks(trello.extract_breaks(comments)))
