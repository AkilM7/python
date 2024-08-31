def space(name):
    for letter in name:
        if letter==' ':
            continue
        else:
            return(False)
            break
    else:
        return(True)
na='  '
print(space(na))
