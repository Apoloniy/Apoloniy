n = int(input("Введите количество чисел n: "));
L = 1;
ch1 = 0;
ch2 = 1;
sum = 1;
while L <= n - 2:
    L = L + 1;
    ch3 = ch1 + ch2;
    sum = sum + ch3;
    s = ch2;
    ch2 = ch3;
    ch1 = s;
print("cумма ряда из " + str(n) + "чисел Фибоначчи:" + str(sum));