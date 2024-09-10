name = 'Rajnikanth'

#string is immutable
l = []
for i in range(len(name)):
    if i == 3:
        l.append('i')
        l.append(name[i])
    else:
        l.append(name[i])
else:
    print(l)
name=''.join(l)
print(name)
