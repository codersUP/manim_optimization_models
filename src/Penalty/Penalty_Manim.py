from manim import *
from .utils import *
import numpy as np
from .penalty_newton import penalty_newton

# inputPath = os.path.abspath(os.path.join(__file__, "../penalty_settings.json"))
# with open(inputPath) as settings:
#     data = json.load(settings)

# _dict = penalty_newton()
# variables, function, constraints = read_json(inputPath)
# lam = sym.Lambda(convert_list_to_tuples(variables), function)
# restrictions_lambdas = [sym.Lambda(convert_list_to_tuples(variables), con) for con in constraints]
# path_dots = read_dots_from_json(_dict["points"])
# p_dots = []
# for (x_, y_) in path_dots:
#     p_dots.append([x_, y_, lam(x_, y_)])


# a = 0
# x1 = np.arange(-100, 150, 10)
# y1 = np.arange(-100, 150, 10)

# try:
#     x_range = data['Penalty_x_range']
#     y_range = data['Penalty_y_range']
# except:
#     raise Exception("You must specify the range of coordinates, i.e x_range = [-4,4], y_range = [0,10]")
class Penalty(ThreeDScene):
    def construct(self):
        inputPath = os.path.abspath(os.path.join(__file__, "../penalty_settings.json"))
        with open(inputPath) as settings:
            data = json.load(settings)
        
        _dict = penalty_newton()
        variables, function, constraints = read_json(inputPath)
        lam = sym.Lambda(convert_list_to_tuples(variables), function)
        restrictions_lambdas = [sym.Lambda(convert_list_to_tuples(variables), con) for con in constraints]
        path_dots = read_dots_from_json(_dict["points"])
        p_dots = []
        for (x_, y_) in path_dots:
            p_dots.append([x_, y_, lam(x_, y_)])
        
        
        a = 0
        x1 = np.arange(-100, 150, 10)
        y1 = np.arange(-100, 150, 10)
        
        try:
            x_range = data['Penalty_x_range']
            y_range = data['Penalty_y_range']
        except:
            raise Exception("You must specify the range of coordinates, i.e x_range = [-4,4], y_range = [0,10]")
        axes = ThreeDAxes(tips=False)
        def shape(u,v):
            z = lam(u, v)
            return np.array([u, v, z])
        graph = Surface(
            shape, v_range=[-2,2], u_range=[-2,2],
            checkerboard_colors=[RED_D, RED_E], resolution=(50, 50), fill_opacity=0.5
        )
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        
        itt_points = [Dot3D(axes.coords_to_point(*i), color=BLUE, radius=0.07) for i in p_dots[1:-1]] # the middle steps points
        ppoints = [Dot3D(axes.coords_to_point(*p_dots[0]), color=RED)]
        ppoints.extend(itt_points)
        ppoints.append(Dot3D(axes.coords_to_point(*p_dots[-1]), color=GREEN))

        self.play(Create(axes))
        self.play(Create(graph))
        method_text = Text(
            f"The point reached was at \n({p_dots[-1][0]}, {p_dots[-1][1]}) \nwith a value of {p_dots[-1][2]}", font_size=20,

        )
        self.add_fixed_in_frame_mobjects(method_text)
        method_text.to_corner(UL)
        
        for p in ppoints:
            self.play(Create(p))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(10)
        self.stop_ambient_camera_rotation()

        self.wait()
        
        
    