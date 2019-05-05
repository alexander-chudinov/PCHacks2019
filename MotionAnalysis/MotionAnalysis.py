import requests
import math
from pyquaternion import Quaternion as quat

url = "https://t-solvies.herokuapp.com/fetch.php"
req = requests.get(url)
tri = req.text.split("|")

'''
signx = -1
switchx = False

signy = -1
switchy = False

signz = -1
switchz = False

ax = []
ay = []
az = []

gx = []
gy = []
gz = []

for i in range(0, len(tri)):
	t = tri[i].split(",")
	if (float(t[0])/131 >= 0 and switchx == False):
		ax.append(float(t[0])/16384/9.81*signx)
	if (float(t[0])/131 >= 0 and switchx == True):
		signx = signx*(-1)
		switchx = False
		ax.append(float(t[0])/16384/9.81*signx)
	if (float(t[0])/131 < 0 and switchx == False):
		switchx == True
		ax.append(float(t[0])/16384/9.81*signx)
	if (float(t[0])/131 < 0 and switchx == True):
		ax.append(float(t[0])/16384/9.81*signx)

	if (float(t[1])/131 >= 0 and switchy == False):
		ay.append(float(t[1])/16384/9.81*signy)
	if (float(t[1])/131 >= 0 and switchy == True):
		signy = signy*(-1)
		switchy = False
		ay.append(float(t[1])/16384/9.81*signy)
	if (float(t[1])/131 < 0 and switchy == False):
		switchy == True
		ay.append(float(t[1])/16384/9.81*signy)
	if (float(t[1])/131 < 0 and switchy == True):
		ay.append(float(t[1])/16384/9.81*signy)

	if (float(t[2])/131 >= 0 and switchz == False):
		az.append(float(t[2])/16384/9.81*signz)
	if (float(t[2])/131 >= 0 and switchz == True):
		signz = signz*(-1)
		switchz = False
		az.append(float(t[2])/16384/9.81*signz)
	if (float(t[2])/131 < 0 and switchz == False):
		switchz == True
		az.append(float(t[2])/16384/9.81*signz)
	if (float(t[2])/131 < 0 and switchz == True):
		az.append(float(t[2])/16384/9.81*signz)


	gx.append(float(t[3])/131)
	gy.append(float(t[4])/131)
	gz.append(float(t[5])/131)

def diff(li):
	rl = [0]
	for i in range(1, len(li)):
		rl.append(li[i]-li[i-1])
	return rl

def integrate(li):
	rl = [li[0]]
	for i in range(1, len(li)):
		rl.append((li[i]+rl[i-1]))
	return rl


angx = integrate(integrate(((gx))))
angy = integrate(integrate(((gy))))
angz = integrate(integrate(((gz))))

vx = [ax[0]]
vy = [ax[1]]
vz = [ax[2]]

for i in range(0, len(angx)):
	angx[i] = math.floor(angx[i])%360 / 180 * math.pi
	angy[i] = math.floor(angy[i])%360 / 180 * math.pi
	angz[i] = math.floor(angz[i])%360 / 180 * math.pi

for i in range(1, len(ax)):
	tr1 = quat(axis=[1, 0, 0], angle=angx[i])
	tr2 = quat(axis=[0, 1, 0], angle=angy[i])
	tr3 = quat(axis=[0, 0, 1], angle=angz[i])
	velocity = tr1.rotate(tr2.rotate(tr3.rotate([ax[i], ay[i], az[i]])))
	vx.append(velocity[0]+vx[i-1])
	vy.append(velocity[1]+vy[i-1])
	vz.append(velocity[2]+vz[i-1])

px = integrate(vx)
py = integrate(vy)
pz = integrate(vz)

file = open("data.txt", "w")

for i in range(0, len(px)):
	file.write("%f,%f,%f;" %(px[i], py[i], pz[i]))

file.close()
'''
ax = []
ay = []
az = []
for i in range (0, len(tri)):
	t = tri[i].split(",")
	ax.append(float(t[0]))
	ay.append(float(t[1]))
	az.append(float(t[2]))

def diff(li):
	rl = [0]
	for i in range(1, len(li)):
		rl.append(li[i]-li[i-1])
	return rl

def integrate(li):
	rl = [li[0]]
	for i in range(1, len(li)):
		rl.append((li[i]+rl[i-1]))
	return rl

px = integrate(integrate(ax))
py = integrate(integrate(ay))
pz = integrate(integrate(az))

file = open("data.txt", "w")

for i in range(0, len(px)):
	file.write("%f,%f,%f;" %(px[i], py[i], pz[i]))

file.close()

x = input()
