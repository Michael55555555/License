import math

def multiply(A, B):
	n = len(A)
	R = [[ 0 for i in range(n) ] for j in range(n) ]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				R[i][j] += A[i][k] * B[k][j]
	return R

def trs(A):
	n = len(A)
	R = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			R[i][j] += A[j][i]
	return R

def scprod(u, v):
	value = 0
	for i in range(len(u)):
		value += (u[i] * v[i])
	return value

def proj(a, b):
	res = [0 for i in range(len(a))]
	alfa = scprod(a,b) / scprod(a, a)
	for i in range(len(a)):
		res[i] = a[i] * alfa
	return res

def norm(v):
	sum = 0
	for i in range(len(v)):
		sum += (v[i] * v[i])
	return math.sqrt(sum)

def subtract (u, v):
	for i in range(len(u)):
		u[i] = u[i] - v[i]
	return u

def QR(A):
	n = len(A)
	Q = [[0 for i in range(n)] for j in range(n)]
	R = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		Q[i] = trs(A)[i]
		for j in range(i):
			Q[i] = subtract(Q[i], proj(Q[j], Q[i]))
	for i in range(n):
		nrm = norm(Q[i])
		for j in range(n):
			Q[i][j] /= nrm
	R = multiply(trs(Q), A)
	return [Q, R]

def read_matrix(n):
	A = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			print("A[" + str(i + 1) + "][" + str(j + 1) + "] = ", end="")
			A[i][j] = int(input())
		print("-------------")
	return A

def pretty_print(A):
	n = len(A)
	for i in range(n):
		for j in range(n):
			print(round(A[i][j], 3), end="\t")
		print()

if __name__ == '__main__':
	print("Introduceti ordinul matricei: \t", end="")
	n = int(input())
	print("Introduceti elementele matricei, in ordine, pe linii:")
	A = read_matrix(n)
	# A = [[3, 2, 1], [4, -1, 2], [-1, 2, 5]]
	[Q, R] = QR(A)
	print()
	print("Descompunerea QR a matricei A:")
	print()
	print("Q = ")
	pretty_print(Q)
	print()
	print("R = ")
	pretty_print(R)
