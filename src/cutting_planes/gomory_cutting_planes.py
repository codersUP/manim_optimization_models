from manim import *
import itertools
import numpy as np
from random import choice
from .utils import GetIntersections, colors # get_intersections_between_two_vmobs
from .cuttingPlanes import bnSolve, gomoryMixedIntegerCut
from .input_parser import load_cp_model

# cut types
# gomoryMixedIntegerCut (may have issues with manim's interpolation, but it's more efficient)
# liftAndProject  (less efficient, but higher cut accuracy)

class Canvas(Scene):
  def construct(self):

    f, constraints, x_range, y_range, module = load_cp_model('./src/cutting_planes/model_cp.json')
    ax = Axes(x_range= x_range+[1], y_range= y_range+[1], tips=True)
    
    # translate the constraints to manim functions, specially if the restriction is of the form x => number, since that is not a function per se
    for constr in constraints:
      if isinstance(constr, tuple):
        type, intersect = constr
        if type == 'v':
          point = ax.coords_to_point(intersect, y_range[1])
          c_ = ax.get_vertical_line(point)
          pass
        if type == 'h':
          c_ = ax.plot(lambda x: intersect, x_range = x_range, use_smoothing=True)
      else:
        print(constr)
        c_ = ax.plot(constr, x_range = x_range, use_smoothing=True)
      #plot 'em all
      self.play(Create(c_))

    # algorithm that generates the cutting planes, as stated in the beggining of the script, there are two methods, liftAndProject, and gomoryMixedIntegerCut
    sol, cc = bnSolve(module,
          whichCuts = [(gomoryMixedIntegerCut, {})],   # this one generates some really odd cuts, and manim is buggy when interpolating those lines with too big coefficients in a small scale
          # whichCuts = [(liftAndProject, {})],    # this one is less efficient and generates multiple repeated cuts
          display = False, debug_print = False, use_cglp = False)
    
    # plot 'em all again
    for lambda_cut, vertical in self.cutToLambda(cc):
      if vertical:
        point = ax.coords_to_point(lambda_cut, 10)
        vline = ax.get_vertical_line(point)
        self.add(vline)
        vline.fade()
      else:
        cutGraph = ax.plot(lambda_cut,x_range= x_range,use_smoothing=True, color=choice(colors))
        self.play(Create(cutGraph))
    

    # some extra fancy objects, the optimal solution and some text with its coordinates
    txt = '('+str( round(sol[0],2) )+','+str( round(sol[1], 2) )+')'
    self.play(Create(ax))
    dot_coords = ax.coords_to_point(*sol)
    sol_dot = Dot(dot_coords, color=RED)
    dot_txt = Text(txt, font_size=20, color= PURE_GREEN)
    self.play(Create(dot_txt))
    self.play(dot_txt.animate.move_to(dot_coords))
    self.play(Create(sol_dot))

        


  @staticmethod
  def cutToLambda(cuts, normalize = False):
    for cut in cuts:
      # the cut has the form ax+by=c
      a,b,c = cut.left.left[0], cut.left.left[1], cut.right
      vertical = False

      if normalize: # normalize the array cuz maybe the coeffs are too big and manim has an issue when interpolating the function values
        m = max([abs(a), abs(b), abs(c)])
        a, b, c = a/m, b/m, c/m


      # case of b = 0, vertical line
      if b == 0:
        lmb, vertical = c / a, True

      # case of a = 0, horizontal line
      elif a == 0:
        lmb = lambda x : c / b

      # case of y = (c-ax)/b
      else:
        lmb = lambda x : (c - (a * x) ) / b

      yield lmb, vertical
    
  @staticmethod
  def innerPoints(intersection_points):
    points = []
    xmin = intersection_points[0][0]
    ymin = intersection_points[0][0]
    xmax = intersection_points[0][0]
    ymax = intersection_points[0][1]
    for point in intersection_points:
      xmin = point[0] if point[0] < xmin else xmin
      ymin = point[1] if point[1] < ymin else ymin
      xmax = point[0] if point[0] > xmax else xmax
      ymax = point[1] if point[1] > ymax else ymax

    xmin = int(xmin) if xmin-int(xmin) < 1e-5 else int(xmin) + 1
    xmax = int(xmax)
    ymin = int(ymin) if ymin-int(ymin) < 1e-5 else int(ymin) + 1
    ymax = int(ymax)

    for i in range(xmin, xmax, 1):
      for j in range(ymin, ymax, 1):
        points.append((i,j))

    return points

  '''
  too inefficient, might delete later
  '''
  @staticmethod
  def get_brute_intersections(functions):
    gt = GetIntersections()
    
    inter = []
    for fi, fj in itertools.combinations(functions,2):
      fi_fj = gt.get_intersections_between_two_vmobs(fi,fj)
      inter.append(fi_fj[0])  # 1 points is more than enough

    return inter

  @staticmethod
  def get_np_intersections(functions, range=(0,10,0.01)):
    inter = []
    xinit, xend, step = range
    x = np.arange(xinit, xend, step)
    for fi, fj in itertools.combinations(functions,2):
      fix = np.array([fi(i) for i in x])
      fjx = np.array([fj(i) for i in x])
      idx = np.argwhere(np.diff(np.sign(fix - fjx))).flatten()  # find the intersections between the functions, all credits to stackOverflow
      fi_fj = [np.array([x[i], fi(x[i])]) for i in idx]  # append the point of intersection
      inter.extend(fi_fj)

    return inter
