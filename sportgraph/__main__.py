import sportgraph.data_provider as data
import sportgraph.plotter as plotter


if __name__ == '__main__':
    x, y = data.get_axis_values()
    plotter.show_line_diagram(x, y)
