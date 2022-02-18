from manim import *
import bab
import json
import numpy as np


class BAB3D(ThreeDScene):
    def add_text_tree(self, root, axes, father=None):
        text_act = Text(
            f"constraints:\n{root['added_constraints']}\nbest point: {root['best_point']}\nevaluation: {root['evaluation']}",
            font_size=10,
        )

        point = Dot3D(
            point=axes.coords_to_point(
                root["best_point"][0], root["best_point"][1], root["evaluation"]
            ),
            color=BLUE,
        )

        self.add(text_act)

        if not father:
            self.add_fixed_in_frame_mobjects(text_act)
            self.play(FadeIn(point), Write(text_act.to_corner(UL)))

        else:
            self.add_fixed_in_frame_mobjects(text_act)
            self.play(
                FadeIn(point),
                Write(text_act.next_to(father, DOWN).align_on_border(LEFT)),
            )

        self.play(point.animate.set_color(GREEN))
        self.wait(1)

        for i in root["childrens"]:
            self.add_text_tree(i, axes, father=text_act)

        self.play(FadeOut(text_act))

    def construct(self):
        f = open("bab.json")
        data = json.load(f)

        func = data["func"]
        vars = data["vars"]
        u_range = data["u_range"]
        v_range = data["v_range"]
        stroke_width = data["stroke_width"]

        if len(vars) != 2:
            raise Exception("the model must have 2 variables")

        m = bab.branch_and_bound_int(**data)
        axes = ThreeDAxes()
        function = Surface(
            lambda u, v: np.array(
                [
                    u,
                    v,
                    bab.func_eval(
                        vars,
                        [u, v],
                        bab.parse_expr(func),
                    ),
                ]
            ),
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

        self.add_text_tree(m["tree"], axes)

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(50)
        self.stop_ambient_camera_rotation()

        self.wait()
