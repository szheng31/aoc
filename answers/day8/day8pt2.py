f = open('input.txt','r')
thelist = f.read().split('\n')
index = 0
theinput = []
for i in thelist:
    theinput.append(i.split())
trialindexes = []
listofindexes = []
accumulator = 0
while True:
    thing = theinput[index]
    
    operation = thing[0]
    value = int(thing[1])
    
    
    if index not in listofindexes:
        listofindexes.append(index)
        if operation == 'jmp':
            trialindex = 0
            theinput[index][0] = 'nop'
            trialindexes = []
            trialaccumulator = 0
            while True:
                if trialindex >= len(theinput):
                    print(trialaccumulator)
                    break
                
                trialthing = theinput[trialindex]
    
                trialoperation = trialthing[0]
                trialvalue = int(trialthing[1])
                if trialindex not in trialindexes:
                    trialindexes.append(trialindex)
                    if trialoperation == 'jmp':
                        trialindex += trialvalue
                    elif trialoperation == 'acc':
                        trialaccumulator += trialvalue
                        trialindex += 1
                    elif trialoperation == 'nop':
                        trialindex += 1
                
                else:
                    break
            theinput[index][0] = 'jmp'
            index += value
        
        
        elif operation == 'acc':
            accumulator += value
            index += 1
        
        elif operation == 'nop':
            trialindex = 0
            theinput[index][0] = 'jmp'
            trialindexes = []
            trialaccumulator = 0
            while True:
                if trialindex >= len(theinput):
                    print(trialaccumulator)
                    break
                
                trialthing = theinput[trialindex]
    
                trialoperation = trialthing[0]
                trialvalue = int(trialthing[1])
                if trialindex not in trialindexes:
                    trialindexes.append(trialindex)
                    if trialoperation == 'jmp':
                        trialindex += trialvalue
                    elif trialoperation == 'acc':
                        trialaccumulator += trialvalue
                        trialindex += 1
                    elif trialoperation == 'nop':
                        trialindex += 1
                else:
                    break
            theinput[index][0] = 'nop'

            index += 1
        
        else:
            print('Error!')
    else:
        break
    
