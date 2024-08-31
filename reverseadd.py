'''
no=12345
while no>0:
    print(no%10)
    no=no//10
'''
n=58777696785
total=0
count=0
while n>0:
    value=n%10
    total=total+value
    n=n//10
    count+=1
else:
    print(total)
    print(count)
