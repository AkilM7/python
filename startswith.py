def startswith(name):
    i=0
    while i<len(name):
        if name[0:3]==start:
            return True
            i+=1
        else:
            return False

name="Sentence"
start="Sen"
print(startswith(name))
