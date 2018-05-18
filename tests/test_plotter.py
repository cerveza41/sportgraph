import unittest
import sportgraph.plotter as plotter


class TestCalculation(unittest.TestCase):
    def test_correct_axis_min_max_calculation(self):
        x = [1, 45, 90, 100]
        y = [1.2, 4.9, 10.2, 3.4]
        result = plotter.calculate_axis(x, y)
        self.assertEqual(result, [1, 100, 0, 10.2])
