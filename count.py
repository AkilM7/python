"""
n="akil"
l='i'

count=0
for r in n:
    if l==r:
        count+=1
    else:
        print(count)
        break
"""
name = 'sunday monday tuesday'
key = 'day'
count = 0
start = 0 
end = len(key)
while start<len(name)-1:
    if name[start:end] == key:
        print("found at", start)
        count+=1
    start+=1
    end+=1
else:
    print(count)

