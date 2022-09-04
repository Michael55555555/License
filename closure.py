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

def equals(A, B):
	n = len(A)
	for i in range(n):
		for j in range(n):
			if A[i][j] != B[i][j]:
				return 0
	return 1

if __name__ == '__main__':
	print("Alegeti tipul de graf: 1 - neorientat, 2 - orientat: \t", end="")
	type = int(input())
	print("Introduceti numarul de noduri ale grafului: \t\t", end="")
	n = int(input())
	if type == 1:
		print("Introduceti numarul de muchii ale grafului: \t\t", end="")
	else:
		print("Introduceti numarul de arce ale grafului: \t\t", end="")
	m = int(input())
	A = [[0 for i in range(n)] for j in range(n)]
	start = 0
	stop = 0
	if type == 1:
		print("Introduceti muchiile grafului in formatul \"nod1 nod2\": ")
	else:
		print("Introduceti arcele grafului in formatul \"nod1 nod2\": ")
	for i in range(m):
		if type == 1:
			print("\tMuchia " + str(i + 1) + ":\t", end="")
		else:
			print("\tArcul " + str(i + 1) + ":\t", end="")
		start, stop = [int(v) for v in input().split()]
		A[start - 1][stop - 1] = 1
		if type == 1:
			A[stop - 1][start - 1] = 1
	T = closure(A)
	if equals(A, T):
		if type == 1:
			print("Inchiderea tranzitiva nu contine muchii nou adaugate.")
		else:
			print("Inchiderea tranzitiva nu contine arce nou adaugate.")
	else:
		if type == 1:
			print("Inchiderea tranzitiva contine muchiile nou adaugate:")
			k = 0
			for i in range(n):
				for j in range(i, n):
					if A[i][j] == 0 and T[i][j] == 1:
						print("\tMuchia " + str(k + 1) + ":\t", end="")
						k = k + 1
						print(i + 1, end=" ")
						print(j + 1)
		else:
			print("Inchiderea tranzitiva contine arcele nou adaugate:")
			k = 0
			for i in range(n):
				for j in range(n):
					if A[i][j] == 0 and T[i][j] == 1:
						print("\tArcul " + str(k + 1) + ":\t", end="")
						k = k + 1
						print(i + 1, end=" ")
						print(j + 1)
