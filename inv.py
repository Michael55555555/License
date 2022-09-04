import math

def multiply(A, B):
	n = len(A)
	R = [[ 0 for i in range(n) ] for j in range(n) ]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				R[i][j] += A[i][k] * B[k][j]
	return R

def invLower(A):
	n = len(A)
	L = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		L[i][i] = 1 / A[i][i]
	for i in range(n):
		for j in range(i):
			for k in range(i):
				L[i][j] -= A[i][k] * L[k][j]
			L[i][j] /= A[i][i]
	return L

def invUpper(A):
	n = len(A)
	R = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		R[i][i] = 1 / A[i][i]
	for i in range(n - 2, -1, -1):
		for j in range(i + 1, n):
			for k in range(i + 1, j + 1):
				R[i][j] -= A[i][k] * R[k][j] / A[i][i]
	return R

def inverseviaQR(A):
	[Q, R] = QR(A)
	return invUpper(R) * transpose(Q)

def inverseviaLU(A):
	[L, U] = LU(A)
	return invLower(U) * invLower(L)

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

def LU(A):
	n = len(A)
	L = [[0 for i in range(n)] for j in range(n)]
	U = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		L[i][i] = 1
	for i in range(n):
		for j in range(n):
			if i > j:
				L[i][j] = A[i][j]
				for k in range(j):		
					L[i][j] -= L[i][k] * U[k][j]
				L[i][j] /= U[j][j]
			else:
				U[i][j] = A[i][j]
				for k in range(i):
					U[i][j] -= L[i][k] * U[k][j]
	return [L, U]

def inv(A):
	[L, U] = LU(A)
	return multiply(invUpper(U), invLower(L))

if __name__ == '__main__':
	print("Introduceti ordinul matricei: \t", end="")
	n = int(input())
	print("Introduceti elementele matricei, in ordine, pe linii:\n")
	A = read_matrix(n)
	I = inv(A)
	print("Inversa matricei I:")
	print()
	print("I = ")
	pretty_print(I)
