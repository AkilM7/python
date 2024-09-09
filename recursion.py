'''
def display(no):
    print(no)
    no+=1
    if no<=5:
        display(no)
display(1)
'''

def sum_of_digits(no,result):
    if no==0:
        return result
    else:
        result=result+no%10
        no=no//10
        return sum_of_digits(no,result)
num=int(input("Enter the Number:"))
abc=int(input("Enter the Number:"))
print(sum_of_digits(num,abc))

