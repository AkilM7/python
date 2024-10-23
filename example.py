for row in range(1,10):
    for col in range (1,10):
        if col==row:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
