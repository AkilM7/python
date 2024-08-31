no = 121
no2 = no
reverse = 0
while no>0:
    #rem = no%10
    reverse = (reverse*10) + no%10
    no = no//10
else:
    if no2 == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")
