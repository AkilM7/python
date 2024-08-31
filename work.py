def calculate_area(length, width):
    if:
        # It's a square room
        area = length * length
    else:
        # It's a rectangular room
        area = length * width
    return area

def calculate(area):
    rate_per_sqr_ft = 10
    charges = area * rate_per_sqr_ft
    return charges

# Example usage:
length = float(input("enter the lenght:"))  # Length of the room
width = float(input("enter the width: "))   # Width of the room (None if square)

# Calculate the area
area = calculate_area(length, width)

# Calculate painting charges
charges = calculate(area)

print("The area of the room square feet is:",area)
print("The painting charges are Rs.",charges)

