name = 'Akil'
d = dict()

for letter in name: 
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] = d.get(letter)+1
else:
    print(d)
