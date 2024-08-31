def lower(name):
    for letter in name:
        if letter>='a' and letter<='z':
            continue
        else:
            print(False)
            break
    else:
        print(True)
name="abcde"
lower(name)
