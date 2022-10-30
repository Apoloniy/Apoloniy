from random import *
P=int(input())
A=[]
for i in range(P):
    B=[]
    for j in range(P):
        B.append(randint(0,100))
    A.append(B)
for i in range(P):
    for j in range(P):
        print(A[i][j],end=" ")
    print()
m=10**10
k=0
for i in range(P):
    for j in range(P):
        if A[i][j]<m:
            m=A[i][j]
            k=i
c=0
for j in range(P):
    c+=A[k][j]
print(c)