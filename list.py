'''
names = ['akil', 'Stella Marys', 1234, True, 5.4]
print(names)

print(names[0])
print(names[-1])

for name in names:
    print(name)

i = 0
while i<len(names):
    print(names[i], end=' ')
    i+=1
print()
----------
days = ['sun','mon','tues']

#output:sunday, monday, tuesday

for day in days:
    print(day+'day', end=' ')
print()
----------
a = [10,20,30]
print(a*2)
---------
#deep copy
a = [10,20,30]


b = a

print(id(a))
print(id(b))

a[1] = 200
print(a[1])
print(b[1])
print(a)
print(b)

-----------
#shallow copy
import copy
a = [10,20,30]
b = copy.copy(a)

print(id(a))
print(id(b))

a[1] = 200
print(a[1])
print(b[1])
print(a)
print(b)
=======
names_a = ['akil', 'ajay']
names = ['joshua', 'sakthivel', 'jecin',names_a]
print(names)
print(len(names))
--------

q = [60,70,36,57]
h = [40,50,60,78,90]
a = [70,80,90]

l = [q,h,a]
print(len(l))
for exams in l:
    for subject in exams:
        print(subject, end=' ')
    print()
---------

a = [10,20,[30],40]
for no in a:
    if type(no) == int:
        print(no)

----------

l = ['libin',5.4, 55, 67]
for element in l:
    if type(element) == str:
        print(element)
---------

q = [60,70,36]
h = [40,50,60]
a = [70,80,90]

l = [q,h,a]

i = 0
while i<len(l):
    print(l[i])
    i+=1

--------
'''
q = [60,70,36,45]
h = [40,50,60,90,100]
a = [70,80,90]

l = [q,h,a]

i = 0
while i<len(l):
    j = 0
    while j<len(l[i]):
        print(l[i][j], end=' ')
        j+=1
    print()
    i+=1
