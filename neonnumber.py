"""
def find_power(base, power):
    result = 1
    while power>0:
        result = result * base
        power-=1
    else:
        return result

def sum_of_digits(num):
    sum =0
    while num>0:
        sum = sum + num%10
        num = num//10
    else:
        return sum


no = 9
output = find_power(no,2)
if no == sum_of_digits(output):
    print(f'{no} is Neon Number')
else:
    print(f'{no} is not Not Neon')
"""


def  Neon_number(no):

    no2=no*no
    sum_of_digit=0
    while no2>0:
       digit=no2%10
       sum_of_digit+=digit
       no2//=10
    return sum_of_digit

no = int(input("Enter the Number : "))
if  Neon_number(no)==no:
    print(f"{no} is a Neon Number" )
else:
    print(f"{no} is Not a  Neon Number")
