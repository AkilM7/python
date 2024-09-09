def find_fact(no):
    if no==1:
        return 1
    else:
        return no* find_fact(no-1)
num=int(input("Enter the Number:"))
print(find_fact(num))
