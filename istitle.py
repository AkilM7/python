def isTitle(sen):
 
    if not (sen[0]>='A' and sen[0]<='Z'):
        return False
    i = 1
    while i<len(sen):
        if sen[i]==' ':
            letter = sen[i+1]
            if letter>='A' and letter<='Z':
                i+=1
                continue
            else:
                return False
        else:
            i+=1
    else:   
        return True
        

sentence = 'Today Is Saturday'

print(isTitle(sentence))
