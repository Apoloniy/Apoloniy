from itertools import count
s = str(input('Введите любоый текст: '));
count = 0
for a in s.split(" "):
    if a.strip()[0] == 'е':
        count = count + 1;
        print(count)    