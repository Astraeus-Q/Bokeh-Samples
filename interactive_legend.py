from bokeh.plotting import figure, show, Column
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, Toggle, CustomJS

Clusters = pd.read_csv("Changing Profits - CSV.csv")
Clusters_cds = ColumnDataSource(Clusters)

# Create a new plot
p = figure(title="Interactive Line Chart", x_axis_label='X-axis', y_axis_label='Y-axis')

# Add line plots
line1 = p.line(x = 'Year', y = "Dept A", source = Clusters_cds, line_color="blue", legend_label="Dept A")
line2 = p.line(x = 'Year', y = "Dept B", source = Clusters_cds, line_color="green", legend_label="Dept B")
line3 = p.line(x = 'Year', y = "Dept C", source = Clusters_cds, line_color="red", legend_label="Dept C")
p.circle(x = 'Year', y = "Dept C", source = Clusters_cds, size=8, fill_color="white", legend_label="Line 2", line_color="red")
bar = p.vbar(x=2018, top=8, width=0.1, color="red", legend_label="Bar", visible = False)
# Set legend click policy to mute
p.legend.click_policy = "mute"

percentage_y3 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0]
hover = HoverTool(renderers=[line3], tooltips=[("Percentage", "@percentage_y3{0.2f}%")])
p.add_tools(hover)

# Create a Toggle widget to show/hide the bar
toggle = Toggle(label="Show Bar", active=False, button_type="success")

# Add a CustomJS callback to toggle the visibility of the bar
toggle.js_on_click(CustomJS(args={'bar': bar}, code="""
    bar.visible = !bar.visible;
"""))
show(Column(p, toggle))
