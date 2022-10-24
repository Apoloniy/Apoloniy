a = [];
for i in range (100):
    a.append(i)
    s = a[0]
    for i in a:
        if i > s and i % 2 == 0:
            s = i
            print(s)