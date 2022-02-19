from src.simplex.manim_model import Simplex2D as X, Simplex3D as Y
<<<<<<< HEAD
from src.line_search.line_search import ThreeDCanvas as lineSearch
from src.cutting_planes.gomory_cutting_planes import Canvas as cuttingPlanes
=======
from src.Numerical_Optimization.manim_numerical_optimization import NO3D, NO2D
from src.Branch_and_Bound.manim_bab import BAB3D, BAB2D
>>>>>>> 9170455d728c49087a9ef621de9886bf7431ce45


class TwoDSimplex(X):
    pass

<<<<<<< HEAD
class LineSearch(lineSearch): pass

class CuttingPlanes(cuttingPlanes): pass
=======

class ThreeDSimplex(Y):
    pass


class ThreeDNO(NO3D):
    pass


class TwoDNO(NO2D):
    pass


class ThreeDBAB(BAB3D):
    pass


class TwoDBAB(BAB2D):
    pass
>>>>>>> 9170455d728c49087a9ef621de9886bf7431ce45
