square = lambda x: x * x

def apply_function(f, x):
    """Apply a function `f` to the value `x`."""
    return f(x)

if __name__ == "__main__":
    print("Square of 4:", apply_function(square, 4))
