f = open('input.txt','r')
thelist = f.read().split('\n')
newlist = []
for i in thelist:
    newlist.append(i.split('contain'))
listOfThingsWithGold = []



for i in newlist:
    
    
    if 'shiny gold bag' in i[1]:
        listOfThingsWithGold.append(i[0][:-2])
print(listOfThingsWithGold)
listofThingsWithThings = []

for i in listOfThingsWithGold:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in listofThingsWithThings:
                pass
            else:
                listofThingsWithThings.append(z[0][:-2])
                
            

listofmorethingswiththings = []
for i in listofThingsWithThings:
    for z in newlist:

        if i in z[1]:
            if z[0][:-2] in listofmorethingswiththings:
                pass
            else:
                listofmorethingswiththings.append(z[0][:-2])
                
print(listofmorethingswiththings)
print(len(listofmorethingswiththings))
x = []
for i in listofmorethingswiththings:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in x:
                pass
            else:
                x.append(z[0][:-2])
print(len(x))
y = []
for i in x:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in y:
                pass
            else:
                y.append(z[0][:-2])
print(len(y))
a = []
for i in y:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in a:
                pass
            else:
                a.append(z[0][:-2])
print(len(a))
b = []
for i in a:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in b:
                pass
            else:
                b.append(z[0][:-2])
print(len(b))
c = []
for i in b:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in c:
                pass
            else:
                c.append(z[0][:-2])
print(len(c))
d = []
for i in c:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in d:
                pass
            else:
                d.append(z[0][:-2])
print(len(d))
e = []
for i in d:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in e:
                pass
            else:
                e.append(z[0][:-2])
print(len(e))
f = []
for i in e:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in f:
                pass
            else:
                f.append(z[0][:-2])
print(len(f))

g = []
for i in f:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in g:
                pass
            else:
                g.append(z[0][:-2])
print(g)
print(len(g))

h = []
for i in g:
    for z in newlist:
        if i in z[1]:
            if z[0][:-2] in h:
                pass
            else:
                h.append(z[0][:-2])

megalist = listOfThingsWithGold + listofThingsWithThings + listofmorethingswiththings + x + y+ a+ b+ c+ d+ e+ f+ g
truelist = []
for i in megalist:
    if i in truelist:
        pass
    else:
        truelist.append(i)


print(len(truelist))
