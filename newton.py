# newton.py

# A script that calculates a root of a quadratic function that has real roots using the Newton-Raphson method

import numpy as np
import random
from math import sqrt
import matplotlib.pyplot as plt

p_i = []
iterations = []
N = 20

def quad(a,b,c):
	p = 5 
	for i in range(N):
		p = p - (a*p**2 + b*p + c)/(2*a*p + b)
		iterations.append(i+1)
		p_i.append(p)
		if i == (N-1):
			print (p)

a = float(input("Enter the x^2 coefficient: "))
b = float(input("Enter the x coefficient: "))
c = float(input("Enter the constant: "))

quad(a,b,c)

plt.plot(iterations, p_i, "r-", label="Newton-Raphson method")

plt.grid(False)
plt.legend()
plt.ylabel("One root of %1.3fx^2" % a + " + %1.3fx + " % b + "%1.3f = 0" % c)
plt.xlabel("Iteration step")
plt.title("Calculating a root of %1.3fx^2" % a + " + %1.3fx + " % b + "%1.3f = 0 \n via the Newton-Raphson method" % c)
plt.savefig("newton-converge.pdf")
plt.show()