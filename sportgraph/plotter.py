import matplotlib as mlp
import matplotlib.pyplot as plt
from typing import List


def calculate_axis(x_values: List[float], y_values: List[float]) -> List[int]:
    min_x = min(x_values)
    max_x = max(x_values)
    min_y = 0
    max_y = max(y_values)
    return [min_x, max_x, min_y, max_y]


def show_line_diagram(x_values: List[float], y_values: List[float]):
    plt.ylabel('Strecke')
    plt.xlabel('Tage')
    blue_line = 'b-'
    plt.plot(x_values, y_values, blue_line)
    plt.axis(calculate_axis(x_values, y_values))
    # activate grid in diagram
    plt.grid(True)
    plt.show()
