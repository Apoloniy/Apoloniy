#вывод и ввод данных матриц из практической работы №9
f=open('D:\TkachenkoEgorMikhailovich_UB21_vvod.txt',"r")
s=open('D:\TkachenkoEgorMikhailovich_UB21_vivod.txt',"w")
A=[]
for line in f:
    a=list(map(int,line.split()))
    A.append(a)
s.write("Задание 8.1\n")
m=10**10
k=0
for i in range(4):
    for j in range(4):
        if A[i][j]<m:
            m=A[i][j]
            k=i
c=0
for j in range(4):
    c+=A[k][j]
s.write("Сумма чисел в строке, содержащей максимальный элемент ")
s.write(str(c))
K=[]
for i in range(4):
    m=1
    for j in range(4):
        m*=A[j][i]
    K.append([m,i])
l=min(K,key=lambda x:x[0])
if l[1]!=4-1:
    for i in range(4):
        A[i][l[1]],A[i][l[1]+1]=A[i][l[1]+1],A[i][l[1]]
else:
    for i in range(4):  
        A[i][l[1]],A[i][l[1]-1]=A[i][l[1]-1],A[i][l[1]]
s.write("\nЗадание 8.2\n")
s.write("Преобразованная матрица\n")
for i in range(4):
    for j in range(4):
        s.write(str(A[i][j]))
        s.write(" ")
    s.write("\n")
s.close()
f.close()

    
    
    
    
    
    
    
    
    



        
