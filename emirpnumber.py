def find_prime(num):
    for div in range(2,num):
        if num%div == 0:
            return False
    else:
        return True

def reverse_no(num):
    rev = 0
    while num>0:
        rem = num%10
        rev = (rev*10) + rem
        num=num//10
    
    return rev

given_number = 11
result = find_prime(given_number)
if result:
    no = reverse_no(given_number)
    result = find_prime(no)
    if result == True:
        print("Emirp Number")
else:
    print("not a emirp number")
