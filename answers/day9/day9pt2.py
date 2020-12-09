from itertools import combinations
f = open('input.txt','r')
thelist = f.read().split('\n')
firstindex = 0
lastindex = 24


while lastindex <= len(thelist):
    validnums = []
    preamble = list(combinations(thelist[firstindex:lastindex + 1],2))

    for i in preamble:
        
        validnums.append(int(i[0])+int(i[1]))


    if lastindex == len(thelist) -1:
        break
    if int(thelist[lastindex+1]) in validnums:
        pass
        
    else:
        x = thelist[lastindex+1]
        
    firstindex += 1
    lastindex += 1
print(x)
listofcontinoussums = []
newlist = []
for i in range(2, len(thelist)):
    for j in range(len(thelist)-i + 1):
        thesum = 0
        listofcontinoussums.append(thelist[j: j + i])
        for z in thelist[j:j+i]:
            thesum += int(z)
        if thesum == int(x):
            print(thelist[j: j + i])
            thelist[j:j+i].sort()
            print(int(thelist[j:j+i][0])+int(thelist[j:j+i][-1]))
