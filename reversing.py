#Reversing given number
no = 1234567
reverse = 0
count_of_digits=0
while no>0:
    rem = no%10
    reverse = (reverse*10) + rem
    no = no//10
    count_of_digits+=1
else:
    print(reverse)
    print(count_of_digits)

i=0
while i<5:
    i+=1
    if i%1==0:
        continue
    print(i)
