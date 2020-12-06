f = open('input.txt','r')
input = f.read().split('\n\n')

newlist = []
listoflistvalues = []
answer = 0
for i in input:
    k = i.split('\n')
    
    
    newlist.append(k)


for i in newlist:
    
    k = ''.join(i)
    listofstuff = []
    for z in k:
        
        if z in listofstuff:
            
            pass
        else:
            listofstuff.append(z)
            
            
    
    for b in listofstuff:
        counter = 0
        
        for x in i:
            
            if b in x:
                counter += 1
            else:
                break
        if counter == len(i):
            answer += 1


    
    
print(answer)
