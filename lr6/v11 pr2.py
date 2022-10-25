a = []
for i in range(20):
    a.append(i)
b=[]
for i in a:
    if i % 2 == 0 and i < 10:
        b.append(i)
if len(b) == 0:
    print("Чисел нет")
else:
    print(b)