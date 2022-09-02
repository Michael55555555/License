	def closure(A):
		n = len(A)
		T = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			T[i][j] = A[i][j]
	for k in range(n):
		for i in range(n):
			for j in range(n):
				T[i][j] = T[i][j] or (T[i][k] and T[k][j])
	return T
