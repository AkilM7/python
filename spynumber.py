'''
def spysum(num1):
    sum = 0   
    while num1 > 0:
        no = num1 % 10
        sum += no
        num1 //= 10
    return sum

def spyproduct(num1):
    product = 1
    while num1 > 0:
        no = num1 % 10
        product *= no
        num1 //= 10
    return product

num1 = int(input("Enter your number: ")) 
sumresult = spysum(num1)
productresult = spyproduct(num1)
   
if sumresult == productresult:
    print("Sum:", sumresult)
    print("Product:", productresult)
    print("It is a spy number")
else:
    print("Sum:", sumresult)
    print("Product:", productresult)
    print("So it is not a Spy number!")

'''

def spynumber(num):
    sum1=0
    product=1
    while num>0:
        no=num%10
        sum1+=no
        product*=no
        num//=10
    return sum1, product
num=int(input("Enter the number:"))
sum1, product=spynumber(num)
print("sum:",sum1)
print("product:",product)
if sum1 == product:
    print("it is spy")
else:
    print("it is not spy" )

