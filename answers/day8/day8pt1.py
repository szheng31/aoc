f = open('input.txt','r')
thelist = f.read().split('\n')
index = 0
theinput = []
for i in thelist:
    theinput.append(i.split())

listofindexes = []
accumulator = 0
while True:
    thing = theinput[index]
    
    operation = thing[0]
    value = int(thing[1])
    
    
    if index not in listofindexes:
        listofindexes.append(index)
        if operation == 'jmp':
            
            index += value
        
        
        elif operation == 'acc':
            accumulator += value
            index += 1
        
        elif operation == 'nop':
            

            index += 1
        
        else:
            print('Error!')
    else:
        
        break
    


print(accumulator)
