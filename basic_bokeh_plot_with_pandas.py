#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

#prepare data
#create in the same folder the file "data.csv"
df = pd.read_csv("data.csv")
x = df["x"]
y = df["y"]

#prepare output file
output_file("line_csv.html")

#create a figure object
f = figure()

#create line plot
f.line(x,y)

#write the plot in the figure object
show(f)
