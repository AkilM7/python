def upper(name):
    for letter in name:
        if letter>='A' and letter<='Z':
            continue
        else:
            print(False)
            break
    else:
        print(True)
name="AKIL"
upper(name)
