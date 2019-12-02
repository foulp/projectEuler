import sys
import numpy as np
from math import sqrt
from scipy import optimize

def dist(x1, y1, x2, y2):
	return sqrt((x1-x2)**2 + (y1-y2)**2)

def total_time(x):
	t0 = dist(0, 0, x[0], 25*(sqrt(2) - 1)) / 10.
	t1 = dist(x[0], 25*(sqrt(2) - 1), x[1], 25*(sqrt(2) - 1) + 10) / 9.
	t2 = dist(x[1], 25*(sqrt(2) - 1) + 10, x[2], 25*(sqrt(2) - 1) + 20) / 8.
	t3 = dist(x[2], 25*(sqrt(2) - 1) + 20, x[3], 25*(sqrt(2) - 1) + 30) / 7.
	t4 = dist(x[3], 25*(sqrt(2) - 1) + 30, x[4], 25*(sqrt(2) - 1) + 40) / 6.
	t5 = dist(x[4], 25*(sqrt(2) - 1) + 40, x[5], 25*(sqrt(2) - 1) + 50) / 5.
	t6 = dist(x[5], 25*(sqrt(2) - 1) + 50, 50*sqrt(2), 50*sqrt(2)) / 10.
	return t0 + t1 + t2 + t3 + t4 + t5 + t6

print optimize.minimize(total_time, (0, 0, 0, 0, 0, 0), tol=1e-10)