from bokeh.plotting import figure, curdoc
from random import random
from bokeh.models import Button
from bokeh.layouts import column

num_circles = 10

#Load your data
x = [random()*70 for i in range(num_circles)]
y = [random()*70 for i in range(num_circles)]

#Generate your plots
p = figure(x_range=(0, 100), y_range=(0, 100))
r = p.circle(x, y, size=5)

#Handle callbacks... use interaction
ds = r.data_source

def add_circle():
    new_data = {}
    new_data['x'] = ds.data['x'] + [random()*70]
    new_data['y'] = ds.data['y'] + [random()*70]

    ds.data = new_data

#Create interactive widgets
b = Button(label='Add circle')
b.on_click(add_circle)

#format/create document
curdoc().add_root(column(b, p))
