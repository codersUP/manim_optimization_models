from src.simplex.manim_model import Simplex2D as X, Simplex3D as Y
from src.Numerical_Optimization.manim_numerical_optimization import NO3D, NO2D
from src.Branch_and_Bound.manim_bab import BAB3D, BAB2D


class TwoDSimplex(X):
    pass


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
