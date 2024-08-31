def isalpha(name):
    i = 0
    while i<len(name):
        if (name[i]>='a' and name[i]<='z')or (name[i]>='A' and name[i]<='Z'):
            pass
        else:
            return False
        i+=1
    else:
        return True

print(isalpha('akil12'))
