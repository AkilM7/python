def space(sentence):
    first = True
    for letter in sentence:
        if letter>='A' and letter<='Z' and first==False:
            print(' '+letter,end='')
        else:
            print(letter,end='')
            first = False

space('HowAreYou')
