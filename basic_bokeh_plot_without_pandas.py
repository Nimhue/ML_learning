pip install bokeh

from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare data
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

#prepare output file
output_file("line.html")

#create a figure object
f = figure()

#create line plot
f.line(x,y)

#create triangle based line plot
#f.triangle(x,y)

#create circle based line plot
#f.circle(x,y)

#write the plot in the figure object
show(f)
