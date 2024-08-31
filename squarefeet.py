def calculate_square(length):
    return length * length

def calculate_rectangle(length, width):
    return length * width

def calculate_triangle(base,height):
    return base*height/2

def calculate_circle(radius):
    return 3.14*radius*radiusu

shape = input("Enter the room shape:")

if shape == 'square':

    length= float(input("Enter the length: "))
    result = calculate_square(length)   

elif shape=='rectangle':

    length = float(input("Enter the Length: "))
    width = float(input("Enter the width: "))
    result = calculate_rectangle(length,width)

elif shape=='triangle':

    base= float(input("Enter the base: "))
    height=float(input("Enter the height: "))
    result= calculate_triangle(b,h)

elif shape=='circle':

    radius= float(input("Enter the radius: "))
    result=calculate_circle(radius)

else:

    print("Invalid syntax?")
   
def calculate(result):
    rate_per_sqr_ft = 10
    charges = result * rate_per_sqr_ft
    return charges

charges = calculate(result)

print(f"The area of the room square feet is:{result}")
print(f"The painting charges are Rs.{charges}")

