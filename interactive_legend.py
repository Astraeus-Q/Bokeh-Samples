from bokeh.plotting import figure, show
import pandas as pd
from bokeh.models import ColumnDataSource

Clusters = pd.read_csv("Changing Profits - CSV.csv")
Clusters_cds = ColumnDataSource(Clusters)

# Create a new plot
p = figure(title="Interactive Line Chart", x_axis_label='X-axis', y_axis_label='Y-axis')

# Add line plots
line1 = p.line(x = 'Year', y = "Dept A", source = Clusters_cds, line_color="blue", legend_label="Dept A")
line2 = p.line(x = 'Year', y = "Dept B", source = Clusters_cds, line_color="green", legend_label="Dept B")
line3 = p.line(x = 'Year', y = "Dept C", source = Clusters_cds, line_color="red", legend_label="Dept C")
p.circle(x = 'Year', y = "Dept C", source = Clusters_cds, size=8, fill_color="white", legend_label="Line 2", line_color="red")

# Set legend click policy to mute
p.legend.click_policy = "mute"

show(p)
