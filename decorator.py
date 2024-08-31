def debug_decorator(fun):
    """Decorator to print function call details."""
    def wrapper(*args, **kwargs):
        print(f"Calling {fun.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = fun(*args, **kwargs)
        print(f"{fun.__name__} returned {result}")
        return result
    return wrapper

@debug_decorator
def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b

if __name__ == "__main__":
    divide(10, 2) 
