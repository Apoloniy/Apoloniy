s = str(input("Введите текст:"));
len = 0;
t_len = 0;
for i in s:
    if i == 'н':
        t_len += 1
    else:
        if len < t_len:
            len = t_len
        t_len = 0
s = s.replace('!','.')
print(len)
print(s)
