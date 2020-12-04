f = open('input.txt','r')
thelist = f.read().split('\n\n')
things = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

answer = 0
splitlist = []
for i in thelist:
    splitlist.append(i.split('\n'))
    
newwerlist = []
for i in splitlist:
    
    newwerlist.append(' '.join(i))
    


finallist = []
for i in newwerlist:
    checker = 0
    for z in things:
        if z in i:
            checker += 1
        else:
            break
    if checker == 7:
        finallist.append(i.split())
            

for i in finallist:#to iterate through each list
    
    jahcounter = 0
    for z in i:#to iterate each list item
        
        keyword = z[0:3]
        keywordvalue = z.split(':')[1]
        if keyword == 'byr':
            if len(z) == 8 and int(keywordvalue) >= 1920 and int(keywordvalue) <= 2002:
                jahcounter += 1
                print('byr worked')
            else:
                break
        elif keyword == 'iyr':
            if len(z) == 8 and int(keywordvalue) >= 2010 and int(keywordvalue) <= 2020:
                jahcounter += 1
                print('iyr worked')
            else:
                break
        elif keyword == 'eyr':
            if len(z) == 8 and int(keywordvalue) >= 2020 and int(keywordvalue) <= 2030:
                jahcounter += 1
                print('eyr worked')
            else:
                break
        elif keyword == 'hgt':
            value = []
            for x in z:
                if x.isdigit():
                    value.append(x)
            value = int(''.join(value))
            
            if z[-2:len(z)] == 'cm':
                
                if value >= 150 and value <= 193:
                    jahcounter += 1
                    print('hgt cm worked')
                else:
                    break


            elif z[-2:len(z)] == 'in':
                if value >= 59 and value <= 76:
                    jahcounter += 1
                    print('in worked')
                else:
                    break
            else:
                break
        elif keyword == 'hcl':
            validcounter = 0
            validcharacters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            if keywordvalue[0] == '#' and len(keywordvalue) == 7:
                for i in keywordvalue[1:]:
                    if i in validcharacters:
                        validcounter += 1
                        
                    else:
                        break
            if validcounter == 6:
                jahcounter += 1
                print('hcl worked')
            else:
                break
        elif keyword == 'ecl':
            validecl = ['amb','blu','brn','gry','grn','hzl','oth']
            if keywordvalue in validecl:
                jahcounter += 1
                print('ecl worked')
            else:
                break
        elif keyword == 'pid':
            if len(keywordvalue) == 9:
                jahcounter += 1
                print('pid worked')
            else:
                break
        elif keyword == 'cid':
            pass
        
        else:
            print('What the fuck did you do',i,jahcounter)
    print(jahcounter)
    if jahcounter == 7:
            answer += 1
    
print(answer)
