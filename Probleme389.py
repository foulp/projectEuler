def v(n):
	"Variance of a n-sided dice"
	return 1.0 * (n+1)*(n-1)/12
def e(n):
	"Expectancy of a n-sided dice"
	return 1.0 * (n+1)/2

"""
E[Z] = E[N] * V[X]
V[Z] = E[N] * V[X] + V[N] * E[X]**2
where Z = SUM_1<=i<=N(X_i) où N est aléatoire
"""

e_t = e(4)  # E[T] = e(4)
v_t = v(4)  # V[T] = v(4)
e_c = e_t * e(6)  # E[C] = E[T]*E[dice6]
v_c = e_t * v(6) + v_t * e(6)**2  # V[C] = E[T]*V[dice6] + V[T]*E²[dice6]
e_o = e_c * e(8)  # E[O] = E[C]*E[dice8]
v_o = e_c * v(8) + v_c * e(8)**2  # V[O] = E[C]*V[dice8] + V[C]*E²[dice8]
e_d = e_o * e(12)  # E[D] = E[O]*E[dice12]
v_d = e_o * v(12) + v_o * e(12)**2  # V[D] = E[O]*V[dice12] + V[O]*E²[dice12]
e_i = e_d * e(20)  # E[I]] = E[D]*E[dice20]
v_i = e_d * v(20) + v_d * e(20)**2  # V[I] = E[D]*V[dice20] + V[D]*E²[dice20]

print(v_i)