from skimage import data, io
from mathTest import makeLa, calculateLa
import matplotlib.pyplot as plt
from pydash import py_, flatten
from math import atan2
import math

from scipy.spatial import KDTree

im=io.imread('/Users/dreday/Downloads/1.pic.jpg', flatten=True)



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
  def slope(self) :
    a = self.p1.y - self.p2.y
    b = self.p1.x - self.p2.x
    return atan2(a, b)
    
  def constan_c(self):
    if abs(self.slope()) == math.pi / 2:
      return self.p1.x
    else:
      return self.p1.y - math.tan(self.slope()) * self.p1.x
  
  def intersection(self,point,slope):
    slope1 = self.slope()
    c = point.y - point.x * math.tan(slope) 
    c1 = self.constan_c()
    if abs(slope1) == math.pi / 2 and slope == math.pi / 2:
      raise Exception('parallel') 
    elif abs(slope1) == math.pi / 2:
      x = self.p1.x
      y = x * math.tan(slope) + c
      return Point(x, y)
    elif abs(slope) == math.pi / 2:
      x = point.x
      y = x * math.tan(slope1) + c1
      return Point(x,y)
    elif slope1 == slope:
      raise Exception('parallel')
    else:
      x = (c - c1) / (math.tan(slope1) - math.tan(slope))
      y = math.tan(slope) * x + c
      return Point(x,y) 


    # radius2 = (point.y ** 2 + point.x ** 2) ** 0.5
    # slope1 = self.slope()
    # radius1 = self.y_axis_intercept()
    # x = (c2 - c1) / (g1 - gradient)
    # y = x * g1 + c1
    # return Point(x,y)
  
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

  def vertical_transversal_dis(self, point):
    line = Line(self.p3, self.p4)
    inter = line.slope()
    
    slope = None
    if inter > 0:
      slope = inter - math.pi / 2
    else:
      slope = inter + math.pi / 2
    intersection = line.intersection(point, slope)

    line2 = Line(self.p1, self.p2)
    intersection2 = line2.intersection(point, slope)
    dis = point_to_point_distance(intersection, intersection2)
    return dis 

  def horizental_transversal_dis(self, point):
    line = Line(self.p3, self.p4)
    slope = line.slope()

    line1 = Line(self.p1, self.p4)
    line2 = Line(self.p2, self.p3)
    p1 = line1.intersection(point, slope)
    p2 = line2.intersection(point, slope)
    return point_to_point_distance(p1,p2)

  def vertical_coordinate(self, point):
    line = Line(self.p3, self.p4)
    return point_to_line_distance(point, line)

  def horizental_coordinate(self, point):
    line = Line(self.p1, self.p4)
    return point_to_line_distance(point, line)
  
  def normalizing_coordinate(self, point):
    h_cor = self.horizental_coordinate(point)
    h_dis = self.horizental_transversal_dis(point)
    v_cor = self.vertical_coordinate(point)
    v_dis = self.vertical_transversal_dis(point)
    return (h_cor / h_dis, v_cor / v_dis)

  def is_point_on_me(self, point):
    area1 = triangle_area(self.p1, self.p2, point)
    area2 = triangle_area(self.p2, self.p3, point)
    area3 = triangle_area(self.p3, self.p4, point)
    area4 = triangle_area(self.p4, self.p1, point)
    sum = area1 + area2 + area3 + area4
    return self.area() == sum
    
  def get_width(self):
    [p3,p4]=[self.p3,self.p4]
    d=point_to_point_distance(p3,p4)
    return round(d)

# line length 
def point_to_point_distance(p1, p2):
	return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

# 点到线的距离 
def point_to_line_distance(point, line):
	area = triangle_area(point, line.p1, line.p2)
	dis = point_to_point_distance(line.p1, line.p2)
	return area * 2 / dis

# def get_width(qua):
#   [p3,p4]=[qua.p3,qua.p4]
#   d=point_to_point_distance(p3,p4)
#   return round(d)




def get_height(qua):
  [p1,p2,p3,p4]=[qua.p1,qua.p2,qua.p3,qua.p4]

  line = Line(p3,p4)
  h1 = round(point_to_line_distance(p1, line))
  h2 = round(point_to_line_distance(p2, line))
  return max(h1, h2)

def generate_rectangle(w, h, la=None):
  arr=[]
  for i in range(h):
    li=[]
    for j in range(w):
      li.append(la)
    arr.append(li)
  return arr

def transform(im, qua):
  points=[]
  for i, li in enumerate(im):
    for j, ele in enumerate(li):
      point = Point(j, i)
      
      if qua.is_point_on_me(point):
        x, y = qua.normalizing_coordinate(point)
        print(x)
        print(y)

  qua_width=qua.get_width()
  rect = generate_rectangle(qua_width, h)

  for i,li in enumerate(rect):
    points=arr[h - i]
    for j,ele in enumerate(li):
      width=len(points)
      la=round((j + 1) / qua_width * width - 1)
      try:
        point=points[la]
      except:
        print(arr[268])
        # print()
      rect[i][j]=im[point.y][point.x]
  return rect
  






##test

p1 = Point(448,499)
p2 = Point(836,708)
p3 = Point(682,927)
p4 = Point(262,655)
qua = Quadrilateral(p1,p2,p3,p4)

w=qua.get_width()
h=get_height(qua)
arr=generate_rectangle(w + 1,h + 1,[])

points = []
eles = []
for i,li in enumerate(im):
  for j,ele in enumerate(li):
    p = Point(j,i)
    if qua.is_point_on_me(p):
      x, y = qua.normalizing_coordinate(p)
      points.append([x * w, y * h])
      eles.append(ele)
    else:
      print(123)
tree = KDTree(points)


for i, li in enumerate(arr):
  for j, ele in enumerate(li):
    try:
      xiabiao=tree.query([j, i])[1]
      arr[i][j] = eles[xiabiao]
    except:arr[i][j]=0





# rect=transform(im, qua)

# # new_im = strech(411, 2700 ,im)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),sharex=True, sharey=True)

ax1.imshow(arr, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('拉伸前', fontsize=20)

ax2.imshow(arr, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('拉伸后', fontsize=20)

fig.tight_layout()

plt.show()
  
  





# b=qua.is_point_on_me(Point(6,6))
# print(b)
