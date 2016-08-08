from skimage import data, io
from mathTest import makeLa, calculateLa
import matplotlib.pyplot as plt
import pydash as _
im=io.imread('/Users/dreday/Downloads/IMG_1345.JPG', flatten=True)

def strech(a, b, img):
	h = len(img)
	w = len(img[0])
	p1 = a
	p2 = b
	la = makeLa(w, h)
	for i, li in enumerate(img):
		cur_p1 = (1 - i / h) * p1
		cur_p2 = p2 + (i / h) * (w - p2)

		# print((i / h) * (w - p2))
		cur_w = cur_p2 - cur_p1
		# print(cur_w)
		for j, ele in enumerate(li):
			if j <= cur_p1 or j >= cur_p2: continue
			rel = j - cur_p1
			quzheng = int(rel / cur_w * w)
			# print(quzheng)
			la[i][quzheng].append(ele)
	
	return calculateLa(la)

def triangle_area(a, b, c):
	ax = a['x']
	ay = a['y']
	bx = b['x']
	by = b['y']
	cx = c['x']
	cy = c['y']
	numerator = ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)
	return abs(numerator / 2)

def quadrilateral_area(a, b, c, d):
	ax = a['x']
	ay = a['y']
	bx = b['x']
	by = b['y']
	cx = c['x']
	cy = c['y']
	dx = d['x']
	dy = d['y']
	numerator = (ax*by-ay*bx) + (bx*cy-by*cx) + (cx*dy -cy*dx) + (dx*ay - dy*ax)
	return abs(numerator / 2)


def lashen(p1, p2, img):
	p1x = p1['x']
	p1y = p1['y']

	p2x = p2['x']
	p2y = p2['y']

	if p1y != 0 and p2y != 0:
		raise Exception("p1 and p2 all not equalt to 0")
	
	

	p3 = {
		'x': len(img[0]),
		'y': 0
	}
	p4 = {
		'x': 0,
		'y': 0
	}

	p3x = len(img[0])
	p3y = 0

	p4x = 0
	p4y = 0

	qua_area = quadrilateral_area(p1,p2,p3,p4)
	for i,li in enumerate(img):
		cur_w = 0
		for j,ele in enumerate(li):
			point = {
				'x': j,
				'y': i
			}
			a1 = triangle_area(point, p1, p2)
			a2 = triangle_area(point, p2, p3)
			a3 = triangle_area(point, p3, p4)
			a4 = triangle_area(point, p4, p1)
			total = a1 + a2 + a3 + a4
			if abs(total - qua_area) < 0.1:
				cur_w+=1
			# print([total, qua_area])
			# if total == qua_area:
			# 	print('good')
			# else:
			# 	print('bad')
		print(cur_w) 
lashen({'x': 100,'y': 0} , {'x': 200,'y':100}, im)


class Point{
	x
	y
}
Point()

def hui
	
		

	# h = len(img)
	# w = len(img[0])
	# p1 = a
	# p2 = b
	# la = makeLa(w, h)
	# for i, li in enumerate(img):
	# 	cur_p1 = (1 - i / h) * p1
	# 	cur_p2 = p2 + (i / h) * (w - p2)
	# 	cur_w = cur_p2 - cur_p1

	# 	for j, ele in enumerate(li):
	# 		if j <= cur_p1 or j >= cur_p2: continue
	# 		rel = j - cur_p1
	# 		quzheng = int(rel / cur_w * w)
	# 		la[i][quzheng].append(ele)
	
	# return calculateLa(la)


new_im = strech(411, 2700 ,im)
# print(new_im)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),sharex=True, sharey=True)

ax1.imshow(im, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('拉伸前', fontsize=20)

ax2.imshow(new_im, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('拉伸后', fontsize=20)

fig.tight_layout()

plt.show()


