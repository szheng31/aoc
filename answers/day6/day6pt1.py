f = open('input.txt','r')
input = f.read().split('\n\n')
print(input)
newlist = []
for i in input:
    k = i.split('\n')
    
    newlist.append(''.join(k))
for z in newlist:
    print(z)
numberofyes = 0
for i in newlist:
    listofstuff = []
    for z in i:
        
        if z in listofstuff:
            pass
        else:
            listofstuff.append(z)
            numberofyes += 1
print(numberofyes)
