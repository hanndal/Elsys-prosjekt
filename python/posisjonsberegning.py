#Hentet fra https://github.com/glucee/Multilateration og gjort noen endringer
from scipy.optimize import minimize
import numpy as np
import math

#posisjonen til de 4 nodene
node1 = (0,0)
node2 = (5,0)
node3 = (5,5)
node4 = (0,5)
h = 2 #høyden til stativene
f = 20*10^6 #klokkefrekvensen, husker ikke hva Elias sa denne var
lydhastigheten = 343

#Har ikke helt peiling på hvordan denne funksjonen fungerer men den virker bra
def finn_posisjon(avstand_til_noder, node_koordinater):
	def error(x, c, r):
		return sum([(np.linalg.norm(x - c[i]) - r[i]) ** 2 for i in range(len(c))])

	l = len(node_koordinater)
	S = sum(avstand_til_noder)
	# compute weight vector for initial guess
	W = [((l - 1) * S) / (S - w) for w in avstand_til_noder]
	# get initial guess of point location
	x0 = sum([W[i] * node_koordinater[i] for i in range(l)])
	# optimize distance from signal origin to border of spheres
	return minimize(error, x0, args=(node_koordinater, avstand_til_noder), method='Nelder-Mead').x

#denne finner avstanden fra noden til steinen (på bakkenivå)
def find_r(tix): #heter kanskje ikke tix (ticks?) men ja
    hyp = tix/f * lydhastigheten
    return math.sqrt(hyp^2 - h^2)

#Vi må finne tix til de fire nodene fra noen csv-filer eller noe(?), så skal resten funke tror jeg
# r1 = find_r(tix1)
# r2 = find_r(tix2)
# r3 = find_r(tix3)
# r4 = find_r(tix4)
#Har funnet fire avstander som 'passer' for å teste programmet, disse må åpenbart byttes ut med de ekte avstandene
r1 = 5.09
r2 = 4.97
r3 = 2.46
r4 = 2.7

if __name__ == "__main__":
	stations = list(np.array([[5,5], [0,5], [5,0], [0,0]]))
	avstand_til_noder = [r1, r2, r3, r4]
	print(finn_posisjon(avstand_til_noder, stations))

#Tada!