def F(A,C):
    m = 0
    q=w=x=y=0
    for i in range(N):
        for j in range(N):
            if A[i][j]>m:
                m=A[i][j]
                x=i
                y=j
    l=0
    for i in range(M):
        for j in range(M):
            if C[i][j]>l:
                l=C[i][j]
                q=i
                w=j 
    A[x][y],C[q][w]=C[q][w],A[x][y]
    print("Преобразованная матрица А")
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=" ")
        print()
    print("Преобразованная матрица C")
    for i in range(M):
        for j in range(M):
            print(C[i][j], end=" ")
        print()
from random import *
N=int(input())
M=int(input())
A=[]
for i in range(N):
    B=[]
    for j in range(N):
        B.append(randint(0,100))
    A.append(B)
C=[]
for i in range(M):
    D=[]
    for j in range(M):
        D.append(randint(0,100))
    C.append(D)
print("Первоначальная матрица А")
for i in range(N):
    for j in range(N):
        print(A[i][j], end=" ")
    print()
print("Первоначальная матрица C")
for i in range(M):
    for j in range(M):
        print(C[i][j], end=" ")
    print()
F(A,C)