'''
row = 1
while row<=9:
    for col in range(1,10):
        print("*", end=' ')
    print()
    row+=1

row = 1
while row<=9:
    col = 1
    while col<=9:
        print("*",end=' ')
        col+=1
    print()
    row+=1

for row in range(1,10):
    for col in range(1,10):
        print("*",end=' ')  
    print()

#I

row = 1
while row<=9:
    col = 1
    while col<=9:
        if row==1 or row==9:
            print("*",end=' ')
        elif col==5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#L: 
row = 1
while row<=9:
    col = 1
    while col<=9:
        if row==9:
            print("*",end=' ')
        elif col==1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#N: 
row = 1
while row<=9:
    col = 1
    while col<=9:
        if col==1 or col==9:
            print("*",end=' ')
        elif col == row:
            print("*",end=' ')
        
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

row = 1
while row<=9:
    col = 1
    while col<=9:
        if col==1 or col==9:
            print("*",end=' ')
        elif col == row:
            print("*",end=' ')
        elif col + row == 10:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#X: 

row = 1
while row<=9:
    col = 1
    while col<=9:
        if col == row:
            print("*",end=' ')
        elif col + row == 10:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1
'''
#Y:
row = 1
while row<=9:
    col = 1
    while col<=9:
        if col == row and row<=5:
            print("*",end=' ')
        elif col + row == 10 and row<=5:
            print("*",end=' ')
        elif col==5 and row>=5:
             print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1
'''
#M: 
row = 1
while row<=9:
    col = 1
    while col<=9:
        if col == 1 or col==9:
            print("*",end=' ')
        elif col == row and row<=5:
            print("*",end=' ')
        elif col + row == 10 and row<=5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#W: 
row = 1
while row<=9:
    col = 1
    while col<=9:
        if col == 1 or col==9:
            print("*",end=' ')
    `   elif col == row and row>=5:
            print("*",end=' ')
        
        elif col + row ==10 and row>=5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#z:
row = 1
while row<=9:
    col = 1
    while col<=9:
        if row == 1 or row ==9:
            print("*",end=' ')
        elif col + row ==10:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#O:
row = 1
while row<=9:
    col = 1
    while col<=9:
        if row == 1 or row ==9:
            print("*",end=' ')
        elif col == 1 or col == 9:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#8:
row = 1
while row<=9:
    col = 1
    while col<=9:
        if row in (1,5,9):
            print("*",end=' ')
        elif col in (1,9):
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#6:
row = 1
while row<=9:
    col = 1
    while col<=9:
        if row in (1,5,9):
            print("*",end=' ')
        elif col == 1: 
            print("*",end=' ')
        elif col == 9 and row>=5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#6:
row = 1
while row<=9:
    col = 1
    while col<=9:
        if row in (1,5,9):
            print("*",end=' ')
        elif col == 1: 
            print("*",end=' ')
        elif col == 9 and row>=5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#D:

row = 1
while row<=9:
    col = 1
    while col<=9:
        if row==1 or row==9:
            if col>=1 and col<9:
                print("*",end=' ')
        elif col==1 or col==9:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#B: 

row = 1
while row<=9:
    col = 1
    while col<=9:
        if row in (1,5,9):
            if col>=1 and col<9:
                print("*",end=' ')
        elif col==1 or col==9:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1

#R:
row = 1
while row<=9:
    col = 1
    while col<=9:
        if row in (1,5):
            if col>=1 and col<9:
                print("*",end=' ')
        elif col==1 or col==9:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        col+=1
    print()
    row+=1   
'''   
