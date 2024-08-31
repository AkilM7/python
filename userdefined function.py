def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b

if __name__ == "__main__":
    print("Addition:", add(10, 5))           
    print("Subtraction:", subtract(10, 5))   
    print("Multiplication:", multiply(10, 5))  
    print("Division:", divide(10, 5)) 
