from src.simplex.manim_model import Simplex2D as X, Simplex3D as Y
from src.Geometric.Geo_Manim import Geo_Manim as G
from src.Penalty.Penalty_Manim import Penalty as P
from src.line_search.line_search import ThreeDCanvas as lineSearch
# from src.cutting_planes.gomory_cutting_planes import Canvas as cuttingPlanes
from src.Numerical_Optimization.manim_numerical_optimization import NO3D, NO2D
from src.Branch_and_Bound.manim_bab import BAB3D, BAB2D

class TwoDSimplex(X): pass
class ThreeDSimplex(Y): pass
class TwoDGeo_Manim(G): pass
class ThreeDPenalty_Manim(P): pass
class LineSearch(lineSearch): pass
# class CuttingPlanes(cuttingPlanes): pass
class ThreeDNO(NO3D):pass
class TwoDNO(NO2D):pass
class ThreeDBAB(BAB3D):pass
class TwoDBAB(BAB2D):pass
