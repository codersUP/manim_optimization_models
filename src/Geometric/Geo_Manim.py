import numpy as np
from .geometric import geometric_aproach
# from .utils import *
import json
from manim import *

# # configure the width and height
# config.frame_width =50
# config.frame_height =50
# w = config.frame_width/7
# h = config.frame_height/7

# x1 = np.arange(-100, 150, 10)
# y1 = np.arange(-100, 150, 10)

# with open('geometric_aproach.json') as settings:
#     data = json.load(settings)
# function_ = data["func"]
# constraints_ = data["constraints"]
# # get all needed to perform the graphics
# (pairs, _lines, m, n, intersections, intersects_evals, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin) = geometric_aproach(constraints_, function_, x1, y1)



# dots = []
# lines = []
# intercepts_dots = []
# intercepts = []
# if Xmax is not None:
#     # initialize the Line classes of Manim to graph
#     for pair in pairs:
#         x_pair, y_pair = pair
#         try:
#             x_i=x_pair[0].p/x_pair[0].q
#             x_e=x_pair[-1].p/x_pair[0].q
#         except:
#             x_i = x_pair[0].item()
#             x_e = x_pair[-1].item()
#         try:
#             y_i= y_pair[0].p/y_pair[0].q
#             y_e= y_pair[-1].p/y_pair[0].q
#         except:
#             y_i = y_pair[0].item()
#             y_e = y_pair[-1].item()
#         init_dot = Dot([x_i/w, y_i/h, 0]).set_color(ORANGE)
#         end_dot = Dot([x_e/w, y_e/h, 0])
#         dots.append(init_dot)
#         dots.append(end_dot)
#         lines.append(Line([x_i/w, y_i/h, 0], [x_e/w, y_e/h, 0]).set_color(ORANGE))

#     # initialize the Dot Classes of Manim to graph
#     for (x, y) in intersections:
#         intercepts_dots.append(Dot([x/w, y/h, 0], stroke_width=10))
#         intercepts.append([x/w, y/h, 0])
#         a = 0

#     # initialize the Text Classes of Manim to graph
#     max_dot = Dot([Xmax/w, Ymax/h, 0], stroke_width=25).set_color(RED)
#     max_text = Text(f'Max: {Zmax} at ({Xmax}, {Ymax}) with red color')
#     min_dot = Dot([Xmin/w, Ymin/h, 0], stroke_width=25).set_color(BLUE)
#     min_text = Text(f'Min: {Zmin} at ({Xmin}, {Ymin}) with blue color')
    

class Geo_Manim(Scene):
    def construct(self):
        # configure the width and height
        config.frame_width =50
        config.frame_height =50
        w = config.frame_width/7
        h = config.frame_height/7

        x1 = np.arange(-100, 150, 10)
        y1 = np.arange(-100, 150, 10)

        inputPath = os.path.abspath(os.path.join(__file__, "../geometric_apreach.json"))
        with open(inputPath, 'r') as settings:
            data = json.load(settings)
        function_ = data["func"]
        constraints_ = data["constraints"]
        # get all needed to perform the graphics
        (pairs, _lines, m, n, intersections, intersects_evals, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin) = geometric_aproach(constraints_, function_, x1, y1)



        dots = []
        lines = []
        intercepts_dots = []
        intercepts = []
        if Xmax is not None:
            # initialize the Line classes of Manim to graph
            for pair in pairs:
                x_pair, y_pair = pair
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
                dots.append(init_dot)
                dots.append(end_dot)
                lines.append(Line([x_i/w, y_i/h, 0], [x_e/w, y_e/h, 0]).set_color(ORANGE))

            # initialize the Dot Classes of Manim to graph
            for (x, y) in intersections:
                intercepts_dots.append(Dot([x/w, y/h, 0], stroke_width=10))
                intercepts.append([x/w, y/h, 0])
                a = 0

            # initialize the Text Classes of Manim to graph
            max_dot = Dot([Xmax/w, Ymax/h, 0], stroke_width=25).set_color(RED)
            max_text = Text(f'Max: {Zmax} at ({Xmax}, {Ymax}) with red color')
            min_dot = Dot([Xmin/w, Ymin/h, 0], stroke_width=25).set_color(BLUE)
            min_text = Text(f'Min: {Zmin} at ({Xmin}, {Ymin}) with blue color')
        
        
        # graph each constraint lines
        for line in lines:
            self.play(Create(line))
        # graph each intersection points
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
        