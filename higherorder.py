def apply_function(f, x):
    """Apply a function `f` to the value `x`."""
    return f(x)

def double(n):
    """Return double the value of `n`."""
    return n * 2

if __name__ == "__main__":
    print("Double of 5:", apply_function(double, 5))
