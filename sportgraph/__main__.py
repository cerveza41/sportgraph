import sportgraph.data_provider as data
import sportgraph.plotter as plotter

if __name__ == '__main__':
    plotter.show_line_diagram(
        data.get_x_axis_values(),
        data.get_y_axis_values()
    )
