s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1 | s2)   #union
print(s1 & s2 )  #intersection
print(s1 ^ s2)   #difference
print(s1.symmetric_difference(s2))

s1.add(25)
print(s1)
s1.remove(10)
print(s1)
print(s1)
print(s1.pop())


