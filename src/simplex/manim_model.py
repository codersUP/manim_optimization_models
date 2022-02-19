from manim import *
# from scipy.optimize._optimize import OptimizeResult
from .simplex_method import *
from .utils import equals, transform2D

class Simplex3D(ThreeDScene):
    def construct(self):
        data, results, ans = call_simplex()
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.generate_constraint_planes(axes, data["A_ineq"], data["b_ineq"], data["ranges"], 0)
        self.generate_constraint_planes(axes, data["A_eq"], data["b_eq"], data["ranges"], 0)
            
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait()
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)

        self.wait(duration=3)


    def generate_constraint_planes(self, axes, matrix, b, ranges, i):
        def constraint(u, v):
            x, y = float(u), float(v)
            [c1, c2, c3] = matrix[i]
            z = (float(b[i]) - float(c1) * x - float(c2) * y) / float(c3)
            return np.array([x, y, z])

        if not matrix is None:
            for _ in range(len(matrix)):
                plane = Surface(
                    constraint,
                    v_range=[-2, +2],
                    u_range=[-2, +2]
                )

                plane.scale(2, about_point=ORIGIN)
                plane.set_style(fill_opacity=1,stroke_color=GREEN)
                plane.set_fill(color=BLUE_C)
                self.add(axes, plane)
                i += 1


class Simplex2D(Scene):
    def construct(self):
        data, results, ans = call_simplex()
        if len(ans.x) > 2:
            data = transform2D(data)
        
        # creating coordinate axes
        ax = Axes(
            x_range=data["ranges"][0],
            y_range=data["ranges"][1],
            # x_axis_config={"numbers_to_include": [round(p.x[0], 2) for p in results]},
            # y_axis_config={"numbers_to_include": [round(p.x[1], 2) for p in results]},
        )

        lines = self.generate_constraint_lines(ax, data["A_ineq"], data["b_ineq"], 0, BLUE_C)
        lines.extend(self.generate_constraint_lines(ax, data["A_eq"], data["b_eq"], 0, ORANGE))
        self.add(ax, *lines)
        self.wait()


        lastPoint = None
        for step in results:
            point = ax.coords_to_point(step.x[0], step.x[1])
            if not lastPoint is None and equals(lastPoint, point):
                continue
            dot = Dot(point=point, color=YELLOW)
            line1 = ax.get_vertical_line(point)
            line2 = ax.get_horizontal_line(point)
            self.add(dot, line1, line2)
            self.wait()
            lastPoint = point

        if ans.status == 0 and ans.success:
            point = ax.coords_to_point(ans.x[0], ans.x[1])
            dot = Dot(point=point, color=RED)
            self.add(dot)
            self.wait()

        self.wait(duration=3)

    
    def generate_constraint_lines(self, ax : Axes, matrix, b, i, color):
        def constraint(x):
            [c1, c2] = matrix[i]
            return (float(b[i]) - float(c1) * x) / float(c2)

        lines = []
        if not matrix is None:
            for _ in range(len(matrix)):
                lines.append(ax.plot(constraint, color=color))
                i += 1

        return lines