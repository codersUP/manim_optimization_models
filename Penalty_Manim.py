from manim import *
from utils import *
import numpy as np
from penalty_newton import penalty_newton

with open('penalty_settings.json') as settings:
    data = json.load(settings)

_dict = penalty_newton()
variables, function, constraints = read_json('penalty_settings.json')
lam = sym.Lambda(convert_list_to_tuples(variables), function)
restrictions_lambdas = [sym.Lambda(convert_list_to_tuples(variables), con) for con in constraints]
path_dots = read_dots_from_json(_dict["points"])
p_dots = []
for (x_, y_) in path_dots:
    p_dots.append([x_, y_, lam(x_, y_)])
# p_dots.append(Dot([*path_dots[-1], lam(*path_dots[-1])], stroke_width=35).set_color(RED_D))


a = 0
# x_ = np.arange(-10,10,1)

# y_ = np.arange(-10,10,1)
# for i in x_:
#     print(str([i, i, lam(i, i)]))
# config.frame_width =50
# config.frame_height =50
# w = config.frame_width/7
# h = config.frame_height/7
x1 = np.arange(-100, 150, 10)
y1 = np.arange(-100, 150, 10)

try:
    x_range = data['Penalty_x_range']
    y_range = data['Penalty_y_range']
except:
    raise Exception("You must specify the range of coordinates, i.e x_range = [-4,4], y_range = [0,10]")
class Penalty(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(tips=False)
        def shape(u,v):
            z = lam(u, v)
            return np.array([u, v, z])
        graph = Surface(
            shape, v_range=[-2,2], u_range=[-2,2],
            checkerboard_colors=[RED_D, RED_E], resolution=(50, 50), fill_opacity=0.5
        )
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        # self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        
        # self.play(Rotate(graph, 0*DEGREES))
        # self.play(Rotate(axes, 0*DEGREES))
        
        itt_points = [Dot3D(axes.coords_to_point(*i), color=BLUE, radius=0.07) for i in p_dots[1:-1]] # the middle steps points
        ppoints = [Dot3D(axes.coords_to_point(*p_dots[0]), color=RED)]
        ppoints.extend(itt_points)
        ppoints.append(Dot3D(axes.coords_to_point(*p_dots[-1]), color=GREEN))

        # self.add(graph, axes)
        self.play(Create(axes))
        self.play(Create(graph))
        method_text = Text(
            f"The point reached was at ({p_dots[-1][0]}, {p_dots[-1][1]}) with a value of {p_dots[-1][2]}"
        )
        self.add_fixed_in_frame_mobjects(method_text)
        method_text.to_corner(UL)
        # self.add(method_text)

        # self.play(Write(method_text.to_corner(UL)))
        
        for p in ppoints:
            # self.add(p)
            self.play(Create(p))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(30)
        self.stop_ambient_camera_rotation()

        self.wait()
        # self.add(axes, graph)
        # self.begin_ambient_camera_rotation(rate=0.7)
        # self.wait(4)
        # self.stop_ambient_camera_rotation()
        # self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.wait()
        
        
    