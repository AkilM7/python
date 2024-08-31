'''
name = "RATHEESH"
print(name)

i = 0
while i<len(name):
    ascii_value = ord(name[i])
    ascii_value = ascii_value + 3
    print(chr(ascii_value),end='')
    i+=1


name = "LIBIN"
print(name)

i = 0
while i<len(name):
    if i%2!=0:
        ascii_value = ord(name[i])
        ascii_value = ascii_value + 1
        print(chr(ascii_value),end='')
    else:
        print(name[i],end='')
    i+=1

name = "RATHEESH"
    # HSEEHTAR

i = len(name) - 1
while i>=0:
    print(name[i],end='')
    i-=1

name = 'abcd'

letter = name[0]  
ascii_value = ord(letter) 
ascii_value = ascii_value - 32  
print(chr(ascii_value)) 
print()   

name = 'Akil,Ajay'

print(chr(ord(name[0]) + 32),end='') 

print(name[1:5],end='')
print(chr(ord(name[5])+32),end="")
print(name[6:],end='')

'''
n="document"
i=0
while i<len(n):
    if i%1==0:
        a=ord(n[i])
        a=(a-32)
        print(chr(a),end="")
    else:
        print(n[i],end='')
    i+=1













