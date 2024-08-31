def endswith(name):
    i=0
    while i<len(name):
        if name[-3:]==start:
            return True
            i+=1
        else:
            return False

name="physical"
start="cal"
print(endswith(name))
