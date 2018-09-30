n = raw_input()
l = []
for i in n:
    if i == '1':
        l.append('9')
    elif i == '9':
        l.append('1')
    else:
        l.append(i)
print(''.join(l))
