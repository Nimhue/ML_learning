#installing missing packages
pip install xlrd

#importing
import pandas
from bokeh.plotting import figure, output_file, show

#accessing the data
df=pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx",sheet_name=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10

#creating the figure and tools
p=figure(plot_width=800,plot_height=700,tools='pan,tap,undo,redo,wheel_zoom,box_zoom,zoom_in,zoom_out,reset')

#plot styling
p.title.text="Temperature and Air Pressure"
p.title.text_color="Black"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color="Black"
p.yaxis.minor_tick_line_color="Red"
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"    

#creating and writing the plot
p.circle(df["Temperature"],df["Pressure"],size=0.8)
output_file("Weather.html")
show(p)
