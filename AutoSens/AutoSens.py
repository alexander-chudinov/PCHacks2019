#state: -1 too low (detects random stuff), 0 perfect, 1 too high (did not detect)
state = 0

import sys
if __name__ == '__main__':
	lo = float(sys.argv[1])
	hi = float(sys.argv[2])
	vl = float(sys.argv[3])

file = open("data.txt", "r")
data = file.read()
file.close()

lo, hi, vl = data.split(",")
#hi is upper bound, lo is lower bound, vl is magnitude of acceleration = cube_root(ax^2+ay^2+ax^2)
#initially, lo = 0, hi = 10, vl = 20


if (state == 0):
	exit()
if (state == -1):
	hold = vl
	vl = (vl+lo)/2
	hi = hold
if (state == 1):
	hold = vl
	vl = (vl+hi)/2
	lo = hold

file = open("data.txt", "w")
file.write("%f,%f,%f" %(lo, hi, vl))
file.close()

print(vl)