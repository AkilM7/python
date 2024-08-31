def idigit(name):
    i = 0
    while i<len(name):
        if (name[i]>='0' and name[i]<='9'):
            pass
        else:
            return False
        i+=1
    else:
        return True

print(isdigit('12'))
