def remove_extra_space(sentence):
    i = 0
    while i <len(sentence):
        if not sentence[i]==' ':
            print(sentence[i],end='')
        else:
            if not sentence[i-1]==' ':
                print(sentence[i],end='')
            else:
                if not sentence[i-2]==' ':
                    print(sentence[i],end='')
        i+=1

sentence = 'abcd             pqrs                   xyz'
remove_extra_space(sentence)
