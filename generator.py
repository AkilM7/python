def count_up_to(max):
    """Generate numbers from 1 up to `max`."""
    count = 1
    while count <= max:
        yield count
        count += 1

if __name__ == "__main__":
    print("Counting up to 3:")
    for number in count_up_to(3):
        print(number)
