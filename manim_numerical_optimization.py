from manim import *
import gradient
import gradient_conj
import newton
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

    def add_text_points_gradient(self, points, axes, text_func, method_text):
        points3d = VGroup()

        for i, point in enumerate(points):
            text_act = Text(
                text_func(point),
                font_size=10,
            )

            point3d = Dot3D(
                point=axes.coords_to_point(
                    point["point"][0], point["point"][1], point["value"]
                ),
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

        self.play(FadeOut(points3d))

    def construct(self):
        f = open("numerical_optimization.json")
        data = json.load(f)

        func = data["func"]
        vars = data["vars"]
        u_range = data["u_range"]
        v_range = data["v_range"]
        stroke_width = data["stroke_width"]

        if len(vars) != 2:
            raise Exception("the model must have 2 variables")

        g = gradient.gradient(**data)
        gc = gradient_conj.gradient_conj(**data)
        n = newton.newton(**data)

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
        )

        self.play(FadeOut(method_text))

        method_text = self.add_method_text("Método de gradiente conjugado")

        self.add_text_points_gradient(
            gc["points"],
            axes,
            lambda p: f"point: {p['point']}\nvalue: {p['value']}\ns: {p['s']}\nalpha: {p['step_arrived']}",
            method_text,
        )

        self.play(FadeOut(method_text))

        method_text = self.add_method_text("Método de Newton")

        self.add_text_points_gradient(
            n["points"],
            axes,
            lambda p: f"point: {p}\nvalue: {func_evaluated(p['point'])}",
            method_text,
        )

        self.play(FadeOut(method_text))

        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.wait(50)
        # self.stop_ambient_camera_rotation()

        self.wait()
