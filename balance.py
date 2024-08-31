'''
balance=8
night=balance//2
print(balance)
balance=balance+night
afternoon=balance//2
print(balance)
balance=balance+afternoon
morning=balance//2
print(balance)
balance=balance+morning
print(balance)

balance=8
balance=balance+balance//2
balance=balance+balance//2
balance=balance+balance//2
print(balance)  

balance=8
count=1
while count<=3:
    balance=balance+balance//2
    count+=1
else:
    print(balance)
'''
name='*'
for no in range (1,6):
    print(name*no)
