a=100
b=1000
div=1
if a<b:
    small=a
else:
    small=b
while div<=small:
    if a% div==0 and b%div==0:
        print(div)
    div +=1
