from ..simplex.simplex_method import simplex_algorithm
from ..simplex.utils import equals
from manim import *

class SimplexExample(Scene):
    def construct(self):
        points = self.linear_problem()
        
        # creating coordinate axes
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 5]
        )

        line1 = ax.plot(lambda x : (3 - x), color=BLUE_C)
        line2 = ax.plot(lambda x : (4 - x) / 2, color=BLUE_C)
        line3 = ax.plot(lambda x : 1 + x, color=BLUE_C)

        self.add(ax)
        self.wait()
        self.add(line1)
        self.wait()
        self.add(line2)
        self.wait()
        self.add(line3)
        
        last = None
        for point in points:
            self.wait()
            p = ax.coords_to_point(point[0], point[1])
            dot = Dot(point=p, color=YELLOW)
            l1 = ax.get_vertical_line(p)
            l2 = ax.get_horizontal_line(p)
            self.add(dot, l1, l2)
            self.wait()

            if not last is None:
                arrow = Arrow(last, dot, buff=0)
                self.add(arrow)
                self.wait()

            last = dot

        dot = Dot(point=last.get_center(), color=RED)
        self.add(dot)
        self.wait(duration=3)


    def linear_problem(self):
        data = {
            "vars_c" : [-2, -3],
            "A_ineq" : [[1, 1], [1, 2], [-1, 1]],
            "b_ineq" : [3, 4, 1],
            "A_eq" : None,
            "b_eq" : None,
            "bounds" : ((0, None), (0, None))
        }
        results, _ = simplex_algorithm(data)
        points = [step.x for step in results]
        ans = [points[0]]
        for i in range(1, len(points)):
            if equals(points[i], points[i - 1]):
                continue
            ans.append(points[i])

        return ans
