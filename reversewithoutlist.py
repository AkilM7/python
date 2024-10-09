sentence = "today is Monday"

reverse = sentence[-1::-1] #yadnoM si yadot
#yadnoM si yadot
#Monday is today
i = 0 
prev = 0
while i<len(reverse):
    if reverse[i] == ' ':
        j = i-1
        while j>=prev:
            print(reverse[j],end='')
            j-=1
        prev = i  
        print(' ',end='')       
   
    i+=1
else:
    print(reverse[len(reverse)-1:prev-1:-1])
