price_dict = {'apple':100, 'pineapple':120, 'orange':110,'banana':100, 'lemon':150}
highest = 0
for fruit_name, price in price_dict.items():
    if price > highest:
        highest = price
        fruit = fruit_name
else:
    print(fruit)
    print(highest)
fruits_list = list(price_dict)

for fruit in fruits_list:
    print(fruit,price_dict[fruit])

for fruit in fruits_list[:2]:
    print(fruit, price_dict[fruit])


l = {no:no*no for no in range(1,6)}
print(l)
