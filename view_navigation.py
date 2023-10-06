import pandas as pd
from bokeh.plotting import curdoc, figure, show
from bokeh.models import ColumnDataSource

Clusters = pd.read_csv("Multiclusters.csv")
Clusters_cds = ColumnDataSource(Clusters)

curdoc().theme = 'dark_minimal'

TOOLS = "pan, wheel_zoom, box_zoom, reset, undo, box_select, lasso_select"

p = figure(title = "Navigation Tools (Pan and Zoom)", plot_height = 800, plot_width = 800, tools = TOOLS)

p.circle(x = 'x', y = 'y', source = Clusters_cds, color = "yellow")

show(p)

