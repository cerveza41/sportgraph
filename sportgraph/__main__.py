from sportgraph.data_provider import DataProvider
import sportgraph.plotter as plotter

if __name__ == '__main__':
    data = DataProvider()
    plotter.show_line_diagram(data.dates, data.distances)
