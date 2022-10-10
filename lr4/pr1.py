A=int(input("Введите число А: "));
B=int(input("Введите число В, которое больше или равно числу А: "));
if A <= B:
    for i in range(A, B+1):
        print(i, end="; ");
else:
    print("Введите А <= B ");    