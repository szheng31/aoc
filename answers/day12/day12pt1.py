f = open('input.txt','r')
actions = f.read().split('\n')
directionlist = ['N','E','S','W']

fowarddirectionindex = 1
fowarddirection = directionlist[fowarddirectionindex]
northcounter = 0
southcounter = 0
eastcounter = 0
westcounter = 0
for i in actions:
    
    direction = i[0]
    distance = int(i[1:])
    if direction == 'F':
        if fowarddirection == 'N':
            northcounter += distance
        elif fowarddirection == 'S':
            southcounter += distance
        elif fowarddirection == 'E':
            eastcounter += distance
        elif fowarddirection == 'W':
            westcounter += distance
        
    elif direction == 'N':
        northcounter += distance

    elif direction == 'S':
        southcounter += distance

    elif direction == 'E':
        eastcounter += distance

    elif direction == 'W':
        westcounter += distance

    elif direction == 'L':
        index = distance / 90
        if index == 1:
            index = 3
        elif index == 3:
            index = 1
        elif index == 4:
            index = 0
        fowarddirectionindex = int(index + fowarddirectionindex)
        if fowarddirectionindex >= len(directionlist):
            fowarddirectionindex -= 4
        fowarddirection = directionlist[fowarddirectionindex]
        
    elif direction == 'R':
        index = distance / 90
        
        fowarddirectionindex = int(index + fowarddirectionindex)
        if fowarddirectionindex >= len(directionlist):
            fowarddirectionindex -= 4
        fowarddirection = directionlist[fowarddirectionindex]

print(abs(northcounter - southcounter)+abs(eastcounter - westcounter))
