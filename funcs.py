from skimage import data, io
from mathTest import makeLa, calculateLa
import matplotlib.pyplot as plt
import pydash as py_
from pydash import flatten
im=io.imread('/Users/dreday/Downloads/IMG_1345.JPG', flatten=True)

def triangle_area(a, b, c):
	ax = a.x
	ay = a.y
	bx = b.x
	by = b.y
	cx = c.x
	cy = c.y
	numerator = ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)
	return abs(numerator / 2)

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Line:
	def __init__(self, p1, p2):
		self.p1 = p1 
		self.p2 = p2

class Quadrilateral:
  def __init__(self, p1, p2, p3, p4):
    self.p1 = p1 
    self.p2 = p2
    self.p3 = p3 
    self.p4 = p4
  
  def area(self):
    ax = self.p1.x
    ay = self.p1.y
    bx = self.p2.x
    by = self.p2.y
    cx = self.p3.x
    cy = self.p3.y
    dx = self.p4.x
    dy = self.p4.y
    numerator = (ax*by-ay*bx) + (bx*cy-by*cx) + (cx*dy -cy*dx) + (dx*ay - dy*ax)
    return abs(numerator / 2)

  def is_point_on_me(self, point):
    area1 = triangle_area(self.p1, self.p2, point)
    area2 = triangle_area(self.p2, self.p3, point)
    area3 = triangle_area(self.p3, self.p4, point)
    area4 = triangle_area(self.p4, self.p1, point)
    sum = area1 + area2 + area3 + area4
    return self.area() == sum

# line length 
def point_to_point_distance(p1, p2):
	return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

# 点到线的距离 
def point_to_line_distance(point, line):
	area = triangle_area(point, line.p1, line.p2)
	dis = point_to_point_distance(line.p1, line.p2)
	return area * 2 / dis

def get_height(qua):
  [p1,p2,p3,p4]=[qua.p1,qua.p2,qua.p3,qua.p4]

  line = Line(p3,p4)
  h1 = round(point_to_line_distance(p1, line))
  h2 = round(point_to_line_distance(p2, line))
  return max(h1, h2)



def transform(im, qua):
  py_.map(enumerate(im))
  
  




# p1 = Point(4,10)
# p2 = Point(11,8)
# p3 = Point(11,2)
# p4 = Point(2,2)
# qua = Quadrilateral(p1,p2,p3,p4)
# b=qua.is_point_on_me(Point(6,6))
# print(b)
