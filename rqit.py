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

def multiply_mv(A, v):
	n = len(A)
	res = [0 for i in range(n)]
	for i in range(n):
		for j in range(n):
			res[i] = res[i] + A[i][j] * v[j]
	return res

def multiply_vm(v, A):
	n = len(A)
	res = [0 for i in range(n)]
	for i in range(n):
		for j in range(n):
			res[i] = res[i] + A[j][i] * v[j]
	return res

def multiply_vv(u, v):
	n = len(A)
	res = 0
	for i in range(n):
		res = res + u[i] * v[i]
	return res

def norm(v):
	sum = 0
	for i in range(len(v)):
		sum += (v[i] * v[i])
	return math.sqrt(sum)

def normalize(v):
	n = len(A)
	res = [0 for i in range(n)]
	norm_value = norm(v)
	for i in range(n):
		res[i] = v[i] / norm_value
	return res

def rq(A):
	b = [1] * n
	for i in range(50):
		b = normalize(multiply_mv(A, b))
		u = multiply_vv(multiply_vm(b, A), b) / multiply_vv(b, b)
	return [b, u]

def read_matrix(n):
	A = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			print("A[" + str(i + 1) + "][" + str(j + 1) + "] = ", end="")
			A[i][j] = int(input())
		print("-------------")
	return A

def pretty_print_v(v):
	n = len(v)
	for i in range(n):
		print(round(v[i], 3), end=" ")

if __name__ == '__main__':
	print("Introduceti elementele matricei, in ordine, pe linii:\t", end="")
	miu = 200
	n = int(input())
	A = read_matrix(n)
	for i in range(n):
		A[i][i] = A[i][i] - miu
	[b, u] = rq(inv(A))
	print("O valoare proprie este:\t u = " + str(round(u, 3)), end="")
	print("\nVectorul propriu asociat este:\t b = ", end="")
	pretty_print_v(b)
	print()
