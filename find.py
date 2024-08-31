name = 'hello world'
key = 'lo'

start = 0 
end = len(key)
while start<len(name)-1:
    if name[start:end] == key:
        print(start)
        break
    start+=1
    end+=1
else:
    print('invalid key')
