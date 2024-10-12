# Normal way

l = ['libin','ajay','akil','joshua','sakthi']
for name in l :
    if name[0] == 'a':
        print(name)


#List Compherhensive

l = ['libin','ajay','akil','joshua','sakthi']
L1=[name for name in l if name[0]=='a']
print(L1)
