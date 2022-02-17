from manim import *
import bab
import json
import numpy as np


class BABPlot(ThreeDScene):
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
        axes.add(point)
        self.add(text_act)

        if not father:
            self.add_fixed_in_frame_mobjects(text_act)
            self.add(text_act.to_corner(UL))
            self.wait()

        else:
            self.add_fixed_in_frame_mobjects(text_act)
            self.add(text_act.next_to(father, DOWN).align_on_border(LEFT))
            self.wait()

        for i in root["childrens"]:
            self.add_text_tree(i, axes, father=text_act)

        # self.play(point.animate.set_color(GREEN))
        self.remove(text_act)

    def construct(self):

        f = open("bab.json")
        data = json.load(f)

        func = data["func"]
        vars = data["vars"]

        if len(vars) == 1:
            pass

        elif len(vars) == 2:
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
                v_range=[-5, 5],
                u_range=[-5, 5],
                checkerboard_colors=[RED_D, RED_E],
                resolution=(50, 50),
            )
            self.renderer.camera.light_source.move_to(
                3 * IN
            )  # changes the source of the light
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

            axes_function = VGroup(axes, function)

            self.play(FadeIn(axes_function))
            self.play(axes_function.animate.move_to(np.array([-10, 1, -2])))

            self.add_text_tree(m["tree"], axes)

            self.wait()
