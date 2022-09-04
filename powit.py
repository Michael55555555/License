import math

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

def powit(A):
	b = [1] * n
	for i in range(20):
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
	n = int(input())
	A = read_matrix(n)
	[b, u] = powit(A)
	print("Cea mai mare valoare proprie:\t u = " + str(round(u, 3)), end="")
	print("\nVectorul propriu asociat este:\t b = ", end="")
	pretty_print_v(b)
	print()
