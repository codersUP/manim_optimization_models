#Librerías necesarias
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, convert_equals_signs
from geometric import geometric_aproach
from utils import *
from manim import *
# from manimlib import *
config.frame_width =50
config.frame_height =50
w = config.frame_width/7
h = config.frame_height/7
x1 = np.arange(-100, 150, 10)
y1 = np.arange(-100, 150, 10)
p1 = np.arange(-100, 150, 10)
# ineqs = []
# ineqs.append(parse_expr('20*x+50*y <= 3000'))
# ineqs.append(parse_expr('x+y <= 90'))
# ineqs.append(parse_expr('y >= 10'))
# ineqs.append(parse_expr('y >= 0'))
# ineqs.append(parse_expr('x >= 0'))
# # la ultima debe ser la de la funcion
# ineqs.append(parse_expr('10000*x+6000*y = 0'))
ineqs = []
ineqs.append('20*x+50*y <= 3000')
ineqs.append('x+y <= 90')
ineqs.append('y >= 10')
ineqs.append('y >= 0')
ineqs.append('0 <= x')
# la ultima debe ser la de la funcion
# ineqs.append('10000*x+6000*y = 0')
equation = parse_expr('10000*x + 6000*y')
# ineqs = []
# ineqs.append(parse_expr('y >= 3'))
# ineqs.append(parse_expr('x <= 20'))
# ineqs.append(parse_expr('2*x+y >= 20')) # y >= 20 - 2*x
# ineqs.append(parse_expr('3*x-2*y >= 7')) # y <= (3*x)/2 - 7/2
# # la ultima debe ser la de la funcion
# ineqs.append(parse_expr('50*x+20*y >= 0'))
# equation = parse_expr('50*x + 20*y')
# converted = get_constraints_cleared(ineqs)

with open('geometric_aproach.json') as settings:
    data = json.load(settings)
function_ = data["func"]
function_ = parse_expr(function_)
constraints_ = data["constraints"]
(pairs, _lines, m, n, intersections, intersects_evals, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin) = geometric_aproach(constraints_, function_, x1, y1)



dots = []
lines = []
intercepts_dots = []
intercepts = []
if Xmax is not None:
    for pair in pairs:
        x_pair, y_pair = pair
        # for i in range(len(x_pair)):
        try:
            x_i=x_pair[0].p/x_pair[0].q
            x_e=x_pair[-1].p/x_pair[0].q
        except:
            x_i = x_pair[0].item()
            x_e = x_pair[-1].item()
        try:
            y_i= y_pair[0].p/y_pair[0].q
            y_e= y_pair[-1].p/y_pair[0].q
        except:
            y_i = y_pair[0].item()
            y_e = y_pair[-1].item()
        init_dot = Dot([x_i/w, y_i/h, 0]).set_color(ORANGE)
        end_dot = Dot([x_e/w, y_e/h, 0])
        # self.add(Dot([6, -10, 0]))
        dots.append(init_dot)
        dots.append(end_dot)
        # dots.append((init_dot, end_dot))
        lines.append(Line([x_i/w, y_i/h, 0], [x_e/w, y_e/h, 0]).set_color(ORANGE))

    for (x, y) in intersections:
        intercepts_dots.append(Dot([x/w, y/h, 0], stroke_width=10))
        intercepts.append([x/w, y/h, 0])
        a = 0

    max_dot = Dot([Xmax/w, Ymax/h, 0], stroke_width=25).set_color(RED)
    max_text = Text(f'Max: {Zmax} at ({Xmax}, {Ymax}) with red color')
    min_dot = Dot([Xmin/w, Ymin/h, 0], stroke_width=25).set_color(BLUE)
    min_text = Text(f'Min: {Zmin} at ({Xmin}, {Ymin}) with blue color')
    

class Geo_Manim(Scene):
    def construct(self):
        
        for line in lines:
            self.play(Create(line))
        for d in intercepts_dots:
            self.play(Create(d))
        if Xmax is not None:
            pol = Polygon(*intercepts).set_fill(RED,opacity=0.5)
            self.play(Create(pol))
            self.play(Create(max_dot))
            self.play(Create(min_dot))
            self.play(Write(max_text))
            self.play(max_text.animate.move_to(DOWN*5))
            self.play(Write(min_text))
            self.play(min_text.animate.move_to(DOWN*3))
            self.wait(3)
        else:
            self.play(Write(Text("There is no Ansewer")))
        