f = open('input.txt','r')
thelist = f.read().split('\n')
thelist = list(map(int,thelist))
thelist.sort()
difonecounter = 0
diftwocounter = 0
difthreecounter = 0
startingoutlet = 0
devicejoltage = thelist[-1] +3

while startingoutlet != devicejoltage:
    for i in thelist:
        if startingoutlet == i - 1:
            difonecounter += 1
            startingoutlet += 1
            break
        elif startingoutlet == i - 2:
            diftwocounter += 1
            startingoutlet += 2
            break
        elif startingoutlet == i-3:
            difthreecounter += 1
            startingoutlet += 3
            break
        elif startingoutlet == devicejoltage -3:
            difthreecounter += 1
            
            startingoutlet = devicejoltage
        else:
            pass

print(difonecounter*difthreecounter)
