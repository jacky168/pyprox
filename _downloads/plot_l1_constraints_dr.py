"""
===================================
Basis Pursuit with Douglas Rachford
===================================

"""
# Author: Samuel Vaiter <samuel.vaiter@ceremade.dauphine.fr>
from __future__ import division
from pyprox.operators import soft_thresholding

print __doc__

# modules
import time

import numpy as np
import pylab as plt

from pyprox import douglas_rachford

# Dimension of the problem
n = 500
p = n//4

# Matrix and observations
A = np.random.randn(p,n)
y = np.random.randn(p,1)

# operator callbacks
F = lambda x: np.linalg.norm(x,1)
ProxF = soft_thresholding
ProxG = lambda x,tau: x + np.dot(A.T, np.linalg.solve(np.dot(A,A.T),
    y - np.dot(A,x)))

t1 = time.time()
x, fx = douglas_rachford(ProxF, ProxG, np.zeros((n,1)),
    maxiter=1000, full_output=1, retall=0, callback=F)
t2 = time.time()
print "Performed 1000 iterations in " + str(t2-t1) + " seconds."

plt.plot(fx)
plt.show()