import requests
import math
from pyquaternion import Quaternion as quat

url = "https://t-solvies.herokuapp.com/fetch.php"
req = requests.get(url)
tri = req.text.split("|")

ax = []
ay = []
az = []

gx = []
gy = []
gz = []

for i in range(0, len(tri)):
	t = tri[i].split(",")
	ax.append(float(t[0])/16384*9.81)
	ay.append(float(t[1])/16384*9.81)
	az.append(float(t[2])/16384*9.81)
	gx.append(float(t[3])/131)
	gy.append(float(t[4])/131)
	gz.append(float(t[5])/131)

def integrate(li):
	rl = [li[0]]
	for i in range(1, len(li)):
		rl.append(li[i]+rl[i-1])
	return rl

angx = (integrate(integrate(gx)))
angy = (integrate(integrate(gy)))
angz = (integrate(integrate(gz)))

for i in range(0, len(angx)):
	angx[i] = math.floor(angx[i])%360 / 180 * math.pi
	angy[i] = math.floor(angy[i])%360 / 180 * math.pi
	angz[i] = math.floor(angz[i])%360 / 180 * math.pi

for i in range(0, len(ax)):
	tr1 = quat(axis=[1, 0, 0], angle=angx[i])
	tr2 = quat(axis=[0, 1, 0], angle=angy[i])
	tr3 = quat(axis=[0, 0, 1], angle=angz[i])
	g_vec = tr1.rotate(tr2.rotate(tr3.rotate([0, 0, -9.81])))
	ax[i] = ax[i] - g_vec[0]
	ay[i] = ay[i] - g_vec[1]
	az[i] = az[i] - g_vec[2]

px = integrate(integrate(ax))
py = integrate(integrate(ay))
pz = integrate(integrate(az))

file = open("data.txt", "w")

for i in range(0, len(px)):
	file.write("%f,%f,%f;" %(px[i], py[i], pz[i]))

file.close()