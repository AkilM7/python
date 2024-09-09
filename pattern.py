'''

for row in range (1,6):
    for col in range (6-row):
        print('*', end=' ')
        
    print()

no=1
for row in range (1,6):
    for col in range (1,7-row):
        print(no, end='  ')
        no+=1
    print()

for row in range (1,6):
    for col in range (1,6-row):
        print('*', end=' ')
    print(1,end=" ")    
    print()

no=1
for row in range (1,6):
    for col in range (1,row+1):
        print(no, end='  ')
        no+=1
    print()

for row in range (1,6):
    for col in range (1,6-row):
        print('*', end=' ')
    for col in range (5):
        print(1,end=' ')
    print()

for row in range (1,6):
    for col in range (1,6-row):
        print('', end=' ')
    for col in range (row):
        print("*",end=' ')
    print()
'''

for row in range (1,6):
    for
