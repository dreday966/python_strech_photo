a0=0.7
a1=0.8

def makeLa(width, height):
	la=[]
	for i in range(height):
		k=[]
		for j in range(width):
			k.append([])
		la.append(k)
	return la
	
def calculateLa(la):
	for i, li in enumerate(la):
		for j, ele in enumerate(li):
			res = 0
			l = len(ele)
			if l != 0:
				sum = 0
				for o in ele:
					sum += o
				res = sum /l 
				la[i][j] = res
			else:
				la[i][j] = 0;
	return la

def map(liOfLi):
	height=len(liOfLi)
	width=len(liOfLi[1])

	la = makeLa(width, height)

	for i, li in enumerate(liOfLi):
		for j, ele in enumerate(li):
			x0 = i / height
			x1 = j / width
			poi = squaretoqua(x0, x1)
			
			y0 = int(poi[0] * width)
			y1 = int(poi[1] * height)
			la[y0][y1].append(ele)
	
	for i, li in enumerate(la):
		for j, ele in enumerate(li):
			res = 0
			l = len(ele)
			if l != 0:
				sum = 0
				for o in ele:
					sum += o
				res = sum / l
			la[i][j] = res

	return la



def quatosquare(y0 , y1):
	denominator = a0 * a1 + a1 * (a1 - 1) * y0 + a0 * (a0 - 1) * y1 
	x0 = (a1 * (a0 + a1 - 1) * y0) / denominator
	x1 = (a0 * (a0 + a1 - 1) * y1) / denominator
	return (x0, x1)

def squaretoqua(x0, x1):
	denominator = (a0 + a1 - 1) + (1 - a1) * x0 + (1 - a0) * x1
	y0 = a0 * x0 / denominator
	y1 = a1 * x1 / denominator
	return (y0, y1)

def topspoint(point, width, height):
	x=point[0]
	y=point[1]
	return (width * x, height * y)

a = squaretoqua(0.4, 0.5)
k = topspoint(a, 100, 100)
print(k)

