# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:05:34 2017

@author: evalero
"""

import numpy as np
import math as mt
import pylab
from edoNumericas import *

#Determinar y(t tal que)
#dy/dt = fde_(t,y) = -(y + 1)(y + 3)
def fde_(t,y):
    f = -(y + 1)*(y + 3)
    return f
#No intervalo 0 <= t <= 2.0
t_0 = 0.0
t_F = 2.0
#Com a cond. inicial y(t=0)=0,5
y_0 = 0.5
# A Solução analítica deste problema e
# y(t) = -3+2(1+e^-2t)^-1
def yde_(t):
    y_ = -3 + 2*(1 + mt.exp(-2 * t))**(-1)
    return y_

def dfdt_(t,y):
    df = y**3 + 6*(y**2) + 11*y + 6
    return df

#Utilizando Taylor de 2da grau com N = 10
N = 10
(t,w) = taylor2EDO(fde_, dfdt_, t_0, t_F, y_0, N)

pylab.figure(3)
pylab.subplot(211)
pylab.plot(t,w,'go--', label="Taylor 2da")
pylab.title("Método de Runge-Kutta de 2da ordem: Ponto Médio")
pylab.xlabel("t")
pylab.ylabel("y")

y = np.ones(t.size)
for i in range(0,t.size):
    y[i] = yde_(t[i])

print ("Método de Taylor 2da Ordem com N=10")
e = errorAbs(t,y,w)

pylab.subplot(212)
pylab.plot(t,e,'go--', label="Taylor 2da")

pylab.xlabel("t")
pylab.ylabel("Erro absoluto")

pylab.show()

#Utilizando RK de 2da ordem com N = 10
N = 10
(t,w) = rk2daOrdem(fde_, t_0, t_F, y_0, N)

pylab.subplot(211)
pylab.plot(t,w,'bo--', label="RK 2da")

print ("Método de Runge-Kutta 2da Ordem com N=10")
errorAbs(t,y,w)
e = errorAbs(t,y,w)

pylab.subplot(212)
pylab.plot(t,e,'bo--', label="RK 2da")
pylab.legend(loc=2)

t = np.linspace(t_0, t_F, N*100)
y = np.ones(t.size)
for i in range(0,t.size):
    y[i] = yde_(t[i])

pylab.subplot(211)
pylab.plot(t,y,'r', label="y(t)")
pylab.legend(loc=2)
