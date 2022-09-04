import sys

def fw(W):
	n = len(W)
	D = [[0 for i in range(n)] for j in range(n)]
	P = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			D[i][j] = W[i][j]
			if W[i][j] > 9000 or i == j:
				P[i][j] = -1
			else:
				P[i][j] = i + 1
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if (D[i][k] + D[k][j] != 9000) and (D[i][j] > D[i][k] + D[k][j]):
					D[i][j] = D[i][k] + D[k][j]
					P[i][j] = P[k][j]
	return [D, P]

def get_route(pred, src, dest):
	if src != dest:
		get_route(pred, src, pred[src - 1][dest - 1])
	print(dest, end=" ")

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
	A = [[sys.maxsize for i in range(n)] for j in range(n)]
	for i in range(n):
		A[i][i] = 0
	start = 0
	stop = 0
	if type == 1:
		print("Introduceti muchiile grafului in formatul \"nod1 nod2 cost\": ")
	else:
		print("Introduceti arcele grafului in formatul \"nod1 nod2 cost\": ")
	for i in range(m):
		if type == 1:
			print("\tMuchia " + str(i + 1) + ":\t", end="")
		else:
			print("\tArcul " + str(i + 1) + ":\t", end="")
		start, stop, cost = [int(v) for v in input().split()]
		A[start - 1][stop - 1] = cost
		if type == 1:
			A[stop - 1][start - 1] = cost
	[dist, pred] = fw(A)
	print("Introduceti nodul sursa si nodul destinatie intre care se va calcula drumul minim in formatul: \"nod_sursa nod_dest\": ")
	src, dest = [int(v) for v in input().split()]
	print("Drumul minim intre nodurile " + str(src) + " si " + str(dest) + ":")
	print("\tva avea costul total de:\t" + str(dist[src - 1][dest - 1]))
	print("\tva avea traseul:\t\t", end="")
	get_route(pred, src, dest)
	print()
