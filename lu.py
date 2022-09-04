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
	[L, U] = LU(A)
	print()
	print("Descompunerea LU a matricei A:")
	print()
	print("L = ")
	pretty_print(L)
	print()
	print("U = ")
	pretty_print(U)


if __name__ == '__main__':
	A = [[3, 2, 1], [4, -1, 2], [-1, 2, 5]]
	[L, U] = LU(A)
