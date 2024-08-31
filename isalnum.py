def isalnum(pincode):
    for letter in pincode:
        if letter>='0' and letter<='9' or (letter>='a' and letter<='z') or (letter>='A' and letter<='Z'):
            continue
        else:
            print(False)
            break
    else:
        print(True)


pincode = "Chennai-600042"
isalnum(pincode)
