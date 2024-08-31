def lcm(a, b):
  
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

num1 = 12
num2 = 18
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")

