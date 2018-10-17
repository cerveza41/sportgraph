import matplotlib as mlp
import matplotlib.pyplot as plt
from typing import List


def calculate_axis(x_values: List[float], y_values: List[float]) -> List[int]:
    min_x = min(x_values)
    max_x = max(x_values)
    min_y = 0
    max_y = max(y_values)
    return [min_x, max_x, min_y, max_y]


def show_line_diagram(days: List[float], distances: List[float], trend: List[float]):
    plt.ylabel('Kilometer')
    plt.xlabel('Tage')

    blue_line_with_dots = 'b-o'
    red_dots = ':r'
    plt.plot(days, distances, blue_line_with_dots, label='Strecke')
    plt.plot(days, trend, red_dots, label='Pausentrend')
    # bin size is set to one week
    bin_size = int(max(days)/7)
    plt.hist(days, bins=bin_size, alpha=0.25,
             color='green', label='Läufe pro Woche')
    plt.axis(calculate_axis(days, distances))

    # activate grid in diagram
    plt.legend()
    plt.grid(True)
    plt.show()
