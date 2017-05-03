# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize
from scipy.optimize import minimize, rosen, rosen_der
import numpy as np
#x0 = [1.2, 1.5, 0.39, 1.33]
#res = minimize(rosen, x0, method='Nelder-Mead', tol=1e-4)
#print res.x


def func(x1):
	return (x1[0]-1)*(x1[0]-1) + x1[1]*x1[1] + x1[2]*x1[2] + np.abs(x1[3]*x1[0]) + np.abs(x1[2]*x1[0])

def test():
	x1 = [6.9, 1.1, 1.1, 0.1]

	res = minimize(rosen, x1, method='Nelder-Mead', tol=1e-8)
	print "Nelder-Mead"
	print "result", res.x
	print "iteration numb", res.nit
	print "----------"

	res = minimize(rosen, x1, method='Powell', tol=1e-8)
	print "Powell"
	print "result", res.x
	print "iteration numb", res.nit
	print "----------"

	res = minimize(rosen, x1, method='CG', tol=1e-8)
	print "CG"
	print  "result", res.x
	print "iteration numb", res.nit
	print "----------"

	res = minimize(rosen, x1, method='BFGS', tol=1e-8)
	print "BFGS"
	print "result", res.x
	print "iteration numb", res.nit
	print "----------"

	#need jacobian
	#res = minimize(rosen, x1, method='Newton-CG', tol=1e-8)
	#print "Newton-CG", "result", res.x, "iteration numb", res.nit

	res = minimize(rosen, x1, method='L-BFGS-B', tol=1e-8)
	print "L-BFGS-B"
	print  "result", res.x
	print "iteration numb", res.nit
	print "----------"

	res = minimize(rosen, x1, method='TNC', tol=1e-8)
	print "TNC"
	print  "result", res.x
	print "iteration numb", res.nit
	print "----------"

	res = minimize(rosen, x1, method='COBYLA', tol=1e-8)
	print "COBYLA"
	print  "result", res.x
	print "iteration numb"#, res.nit\
	print "----------"

	res = minimize(rosen, x1, method='SLSQP', tol=1e-8)
	print "SLSQP"
	print  "result", res.x
	print "iteration numb", res.nit
	print "----------"

	#need jacobian
	#res = minimize(rosen, x1, method='dogleg', tol=1e-8)
	#print "dogleg", "result", res.x, "iteration numb"

	#need jacobian
	#res = minimize(rosen, x1, method='trust-ncg', tol=1e-8)
	#print "trust-ncg", "result", res.x, "iteration numb"

if __name__=='__main__':
	test()