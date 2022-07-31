#!/usr/bin/python3
from math import ceil
import scipy.optimize

def compute(V):
	if len(V) <= 1:
		return
	def h(x):
		return sum([x**(-v) for v in V])-1
	X = scipy.optimize.brenth(h,1, 100)
	return X

def calc(b,c,d):
	X = []
#B2
	X.append(compute([1,b-2*c]))
	X.append(compute([1,c]))
	X.append(compute([1,2*d]))
#B4
	X.append(compute([1,1,1+b-3*d,b-2*d]))
	X.append(compute([1,1,1+b-3*d,2*b-c-2*d]))
#B5
	X.append(compute([1,1,1,2*b-2*c-3*d]))
#B7
	X.append(compute([1,1,1+(b-c-2*d)*1,1+b-c-d,2*b-2*c-2*d]))
	X.append(compute([1,1,1+(b-c-2*d)*1,1+2*b-c-4*d,2*b-c-3*d]))
	X.append(compute([1,1,1+(b-c-2*d)*1,1+2*b-2*c-3*d,3*b-2*c-5*d]))

# Rules B1, B3, and B6 have branching numbers 2, 5, and 5
	X.append(5)

	return max(X)**(1+b),X

best_Y = 999
t = 10
for b0 in range(40*t,60*t+1):
	for d0 in range(5*t,7*t+1):
		b = b0/(100*t)
		d = d0/(100*t)
		c = 2*d
		if not d <= c <= b: continue
		if b-2*c-2*d < 0.01: continue
		Y,X = calc(b,c,d)
		if Y < best_Y:
			best_Y = Y
			best_b = b
			best_c = c
			best_d = d
			best_X = X

print(best_b,best_c,best_d,ceil(best_Y*10000)/10000,ceil(max(best_X)*10000)/10000)
