import numpy as np
import pandas as pd
import math

h = 2 #høyden på stativet
f = 16*10^6 #klokkefrekvens (?)
lydhastighet = 343 #lydhastighet
nodes = 4 #antall noder
nodePositions = {(0,0), (5,0), (5,5), (5,0)} #posisjonen til nodene
circles = {}

class Circle:
  def __init__(self, x, y, r):
    self.y = y
    self.x = x
    self.r = r

tix_node1 = pd.read_csv('tix_node1.csv')
tix_node2 = pd.read_csv('tix_node2.csv')
tix_node3 = pd.read_csv('tix_node4.csv')
tix_node4 = pd.read_csv('tix_node4.csv')

tix_nodes = {tix_node1, tix_node2, tix_node3, tix_node4}

for tix_node in tix_nodes:
    r = find_r() #legg inn data for tix her
    #legg dette til som en Circle-objekt i en liste over sirklene(?)
    
def find_r(t):
    hyp = t/f * lydhastighet
    return math.sqrt(h^2 - hyp^2)

def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2) #avstanden 
    a=(r0**2-r1**2+d**2)/(2*d)
    h=math.sqrt(r0**2-a**2)

    #Finner skjæringen mellom linjen mellom nodene og linjen som går mellom de to skjæringspunktene
    x_rel=x0+a*(x1-x0)/d   
    y_rel=y0+a*(y1-y0)/d 

    #Legger til eller trekker fra 'høyden'/avstanden fra det relative punktet
    x_first=x_rel+h*(y1-y0)/d     
    y_first=y_rel-h*(x1-x0)/d 

    #Legger til eller trekker fra (motsatt fra forrige punkt) til det relative punktet
    x_second=x_rel-h*(y1-y0)/d
    y_second=y_rel+h*(x1-x0)/d

    #Returnerer de to punktene
    return (x_first, y_first, x_second, y_second)

for n in range(circles):
    intersections = get_intersections(circles[n], circles[n+1])



    
    





