import pandas as pd
from bokeh.plotting import gridplot, figure, show
from bokeh.models import ColumnDataSource, CustomJS

Clusters = pd.read_csv("Property.csv")
Clusters_cds = ColumnDataSource(Clusters)

# curdoc().theme = 'dark_minimal'

TOOLS = "pan, wheel_zoom, box_zoom, reset, undo, box_select, lasso_select"

p1 = figure(title = "Distance from MRT", plot_height = 400, plot_width = 400, tools = TOOLS)
p2 = figure(title = "Age of Property", plot_height = 400, plot_width = 400, tools = TOOLS)
p3 = figure(title = "Number of Convenience Stores", plot_height = 400, plot_width = 400, tools = TOOLS)
p4 = figure(title = "Longitude", plot_height = 400, plot_width = 400, tools = TOOLS)



p1.circle(x = 'MRT', y = 'Price', source = Clusters_cds, color = "blue")
p2.circle(x = 'Age', y = 'Price', source = Clusters_cds, color = "red")
p3.circle(x = 'Store', y = 'Price', source = Clusters_cds, color = "green")
p4.circle(x = 'Longitude', y = 'Price', source = Clusters_cds, color = "purple")

# Link selection between plots
# Clusters_cds.selected.js_on_change('indices', CustomJS(args=dict(s1=Clusters_cds, s2=Clusters_cds, s3=Clusters_cds), code="""
#     s2.selected.indices = s1.selected.indices;
#     s3.selected.indices = s1.selected.indices;
# """))

# Clusters_cds.selected.js_on_change('indices', CustomJS(args=dict(s1=Clusters_cds, s2=Clusters_cds, s3=Clusters_cds), code="""
#     s1.selected.indices = s2.selected.indices;
#     s3.selected.indices = s2.selected.indices;
# """))

# Clusters_cds.selected.js_on_change('indices', CustomJS(args=dict(s1=Clusters_cds, s2=Clusters_cds, s3=Clusters_cds), code="""
#     s1.selected.indices = s3.selected.indices;
#     s2.selected.indices = s3.selected.indices;
# """))


grid = gridplot([[p1, p2, p3, p4]])
show(grid)

