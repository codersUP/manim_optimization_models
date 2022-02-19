from manim import *
from .gradient import gradient
from .gradient_conj import gradient_conj
from .newton import newton
import json
import sympy as sp
import numpy as np


class NO3D(ThreeDScene):
    def add_method_text(self, text):
        method_text = Text(
            text,
            font_size=20,
        )
        self.add(method_text)

        self.add_fixed_in_frame_mobjects(method_text)
        self.play(Write(method_text.to_corner(UL)))

        return method_text

    def add_text_points_gradient(
        self, points, axes, text_func, method_text, get_coordintes, delete_points=True
    ):
        points3d = VGroup()

        for i, point in enumerate(points):
            text_act = Text(
                text_func(point),
                font_size=10,
            )

            point3d = Dot3D(
                point=axes.coords_to_point(*get_coordintes(point)),
                color=BLUE,
            )

            points3d += point3d

            self.add(text_act)

            self.add_fixed_in_frame_mobjects(text_act)
            self.play(
                FadeIn(point3d),
                Write(text_act.next_to(method_text, DOWN).align_on_border(LEFT)),
            )
            self.play(point3d.animate.set_color(GREEN), FadeOut(text_act))
            self.wait(1)

        if delete_points:
            self.play(FadeOut(points3d))

    def construct(self):
        inputPath = os.path.abspath(os.path.join(__file__, "../input.json"))
        with open(inputPath, "r") as fp:
            data = json.load(fp)

        func = data["func"]
        vars = data["vars"]
        u_range = data["u_range"]
        v_range = data["v_range"]
        stroke_width = data["stroke_width"]

        if len(vars) != 2:
            raise Exception("the model must have 2 variables")

        g = gradient(**data)
        gc = gradient_conj(**data)
        n = newton(**data)

        func = sp.parse_expr(func)
        func_lambda = sp.Lambda(vars, func)
        func_evaluated = lambda x: np.array([func_lambda(*x)], dtype=float)

        axes = ThreeDAxes()
        function = Surface(
            lambda u, v: np.array([u, v, func_evaluated((u, v))]),
            u_range=u_range,
            v_range=v_range,
            checkerboard_colors=[RED_D, RED_E],
            resolution=(50, 50),
            fill_opacity=0.5,
            stroke_width=stroke_width,
        )
        self.renderer.camera.light_source.move_to(
            3 * IN
        )  # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        axes_function = VGroup(axes, function)

        self.play(FadeIn(axes_function))

        method_text = self.add_method_text("Método de gradiente (Máximo Descenso)")

        self.add_text_points_gradient(
            g["points"],
            axes,
            lambda p: f"point: {p['point']}\nvalue: {p['value']}\ngradient: {p['gradient']}\nalpha: {p['step_arrived']}",
            method_text,
            get_coordintes=lambda point: [
                point["point"][0],
                point["point"][1],
                point["value"],
            ],
        )

        self.play(FadeOut(method_text))

        method_text = self.add_method_text("Método de gradiente conjugado")

        self.add_text_points_gradient(
            gc["points"],
            axes,
            lambda p: f"point: {p['point']}\nvalue: {p['value']}\ns: {p['s']}\nalpha: {p['step_arrived']}",
            method_text,
            get_coordintes=lambda point: [
                point["point"][0],
                point["point"][1],
                point["value"],
            ],
        )

        self.play(FadeOut(method_text))

        method_text = self.add_method_text("Método de Newton")

        self.add_text_points_gradient(
            n["points"],
            axes,
            lambda p: f"point: {p}\nvalue: {func_evaluated(p)}",
            method_text,
            get_coordintes=lambda point: [
                point[0],
                point[1],
                func_evaluated(point),
            ],
            delete_points=False,
        )

        self.play(FadeOut(method_text))

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(50)
        self.stop_ambient_camera_rotation()

        self.wait()


class NO2D(Scene):
    def add_method_text(self, text):
        method_text = Text(
            text,
            font_size=20,
        )
        self.add(method_text)

        self.play(Write(method_text.to_corner(UL)))

        return method_text

    def add_text_points_gradient(
        self, points, axes, text_func, method_text, get_coordintes, delete_points=True
    ):
        points2d = VGroup()

        for i, point in enumerate(points):
            text_act = Text(
                text_func(point),
                font_size=10,
            )

            point2d = Dot(
                point=axes.coords_to_point(*get_coordintes(point)),
                color=RED,
            )

            points2d += point2d

            self.add(text_act)

            self.play(
                FadeIn(point2d),
                Write(text_act.next_to(method_text, DOWN).align_on_border(LEFT)),
            )
            self.play(point2d.animate.set_color(GRAY), FadeOut(text_act))
            self.wait(1)

        if delete_points:
            self.play(FadeOut(points2d))

    def construct(self):
        inputPath = os.path.abspath(os.path.join(__file__, "../input.json"))
        with open(inputPath, "r") as fp:
            data = json.load(fp)

        func = data["func"]
        vars = data["vars"]
        u_range = data["u_range"]
        v_range = data["v_range"]

        if len(vars) != 1:
            raise Exception("the model must have 1 variable1")

        func = sp.parse_expr(func)
        func_lambda = sp.Lambda(vars, func)
        func_evaluated = lambda x: np.array([func_lambda((x))], dtype=float)

        g = gradient(**data)
        gc = gradient_conj(**data)
        n = newton(**data)

        axes = Axes(
            x_range=[u_range[0], u_range[1], 1],
            y_range=[v_range[0], v_range[1], 1],
            x_length=abs(u_range[1] - u_range[0]),
            axis_config={"color": GREEN},
        )
        axes_labels = axes.get_axis_labels()

        function = axes.plot(lambda x: func_evaluated(x), color=BLUE)

        axes_function = VGroup(axes, axes_labels, function)

        self.play(FadeIn(axes_function))

        method_text = self.add_method_text("Método de gradiente (Máximo Descenso)")

        self.add_text_points_gradient(
            g["points"],
            axes,
            lambda p: f"point: {p['point']}\nvalue: {p['value']}\ngradient: {p['gradient']}\nalpha: {p['step_arrived']}",
            method_text,
            get_coordintes=lambda point: [
                point["point"][0],
                point["value"],
            ],
        )

        self.play(FadeOut(method_text))

        method_text = self.add_method_text("Método de gradiente conjugado")

        self.add_text_points_gradient(
            gc["points"],
            axes,
            lambda p: f"point: {p['point']}\nvalue: {p['value']}\ns: {p['s']}\nalpha: {p['step_arrived']}",
            method_text,
            get_coordintes=lambda point: [
                point["point"][0],
                point["value"],
            ],
        )

        self.play(FadeOut(method_text))

        method_text = self.add_method_text("Método de Newton")

        self.add_text_points_gradient(
            n["points"],
            axes,
            lambda p: f"point: {p}\nvalue: {func_evaluated(*p)}",
            method_text,
            get_coordintes=lambda point: [
                point[0],
                func_evaluated(*point),
            ],
            delete_points=False,
        )

        self.play(FadeOut(method_text))

        self.wait()
