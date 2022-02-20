from src.simplex.manim_model import Simplex2D as X, Simplex3D as Y
# from src.geometric.Geo_Manim import Geo_Manim as G
from src.penalty.penalty_manim import Penalty as P
from src.line_search.line_search import ThreeDCanvas as lineSearch
from src.cutting_planes.gomory_cutting_planes import Canvas as cuttingPlanes
from src.numerical_optimization.manim_numerical_optimization import NO3D, NO2D
from src.branch_and_bound.manim_bab import BAB3D, BAB2D
from src.geom_ideas.simplexEx import SimplexExample as SE

class TwoDSimplex(X): pass

class ThreeDSimplex(Y): pass

# class TwoDGeo_Manim(G): pass

class ThreeDPenalty_Manim(P): pass

class LineSearch(lineSearch): pass

class CuttingPlanes(cuttingPlanes): pass

class ThreeDNO(NO3D):pass

class TwoDNO(NO2D):pass

class ThreeDBAB(BAB3D):pass

class TwoDBAB(BAB2D):pass

class GeoSimplex(SE): pass

