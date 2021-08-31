import numpy as np

#1行目のN,Mを取得する
N,M = input().strip().split()
N,M = [int(N),int(M)] 

#配列
a = [int(input()) for i in range(M)]
A = np.array(a)

b = [int(input()) for i in range(N * M)]
B = np.array_split(b, N)

#配列計算
C = A - B

Z=100
for N in range(len(C)):
    for M in range(len(C[N])):
        if abs(C[N][M]) <= 5:
            Z = Z
        elif 5 < abs(C[N][M]) <= 10:
            Z = Z-1
        elif 10 < abs(C[N][M]) <= 20:
            Z = Z-2
        elif 20 < abs(C[N][M]) <= 30:
            Z = Z-3
        else:
            Z = Z-5

print(A)
print(B) 
print(C)
print(C[0][0])
print(Z)
