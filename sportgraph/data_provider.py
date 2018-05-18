from datetime import date
from typing import List


def transform_dates(dates: List[date]) -> List[int]:
    lowest_date = min(dates)
    diffs_to_lowest_date = []
    for d in dates:
        diffs_to_lowest_date.append((d-lowest_date).days)
    return diffs_to_lowest_date


def get_x_axis_values() -> List[int]:
    dates = []
    dates.append(date(2017, 12, 19))
    dates.append(date(2017, 12, 28))
    dates.append(date(2018, 1, 2))
    dates.append(date(2018, 1, 8))
    dates.append(date(2018, 1, 15))
    dates.append(date(2018, 1, 22))
    dates.append(date(2018, 1, 30))
    dates.append(date(2018, 2, 5))
    dates.append(date(2018, 2, 20))
    dates.append(date(2018, 2, 26))
    dates.append(date(2018, 3, 20))
    dates.append(date(2018, 4, 5))
    dates.append(date(2018, 4, 17))
    dates.append(date(2018, 4, 23))
    dates.append(date(2018, 4, 29))
    dates.append(date(2018, 5, 1))
    dates.append(date(2018, 5, 8))
    dates.append(date(2018, 5, 13))
    dates.append(date(2018, 5, 16))
    dates.append(date(2018, 5, 18))

    return transform_dates(dates)


def get_y_axis_values() -> List[int]:
    return [1.85, 1.90, 2.00, 2.5, 2.06, 2.26, 2.48, 2.08, 2.6,
            2.77, 2.48, 2.90, 1.47, 2.80, 2.24, 3.0, 2.67, 3, 3.22, 3.3]
