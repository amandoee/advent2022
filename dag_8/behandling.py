x = []
y= []

boolx = []
booly = []

viewsx = []
viewsy=[]


with open("input.txt") as input2:
    for line in input2:
        x = []
        boolx = []
        for char in line:
            if str(char) != "\n":
                x.append(char)
                boolx.append(False)
        y.append(x)
        booly.append(boolx)



def find_nummer(række_nummer,kolonne_nummer):
    nummer=int(y[række_nummer][kolonne_nummer])

    left=1
    right=1
    up=1
    down=1

    for i in reversed(range(0,kolonne_nummer)):
        sammenlign=int(y[række_nummer][i])
        if (int(y[række_nummer][i])<nummer):
            left+=1
            if i==0:
                left-=1
        else:
            break
    
    for j in range(kolonne_nummer+1,len(y[0])):
        sammenlign=int(y[række_nummer][j])
        if (int(y[række_nummer][j])<nummer):
            right+=1
            if j==len(y[0])-1:
                right-=1
        else:
            break
    
    for k in reversed(range(0,række_nummer)):
        sammenlign=int(y[k][kolonne_nummer])
        if (int(y[k][kolonne_nummer])<nummer):
            up+=1
            if (k==0):
                up-=1
        else:
            break
           
    for l in range(række_nummer+1,len(y)):
        sammenlign=int(y[l][kolonne_nummer])
        if (int(y[l][kolonne_nummer])<nummer):
            down+=1
            if l==len(y)-1:
                down-=1
        else:
            break
    
    return left*right*up*down



#Rundt langs kanten
for i in range(len(x)):
    for j in range(len(y[i])):
        if i == 0 or i == len(x)-1 or j == 0 or j == len(y[i])-1:
            (booly[j])[i]=True


#Øvre kant
for i in range(len(x)):
    highest_height=0
    for j in range(len(y[i])):
        højde = int((y[j])[i])
        if int((y[j])[i]) > highest_height:
            (booly[j])[i]=True
            highest_height = int((y[j])[i])
    

#Nedre kant
for i in range(len(x)):
    a=len(x)-i-1
    highest_height=0
    for j in range(len(y[i])):
        b=len(y[i])-j-1
        højde = int((y[b])[i])
        if int((y[b])[i]) > highest_height:
            (booly[b])[i]=True
            highest_height = int((y[b])[i])


#Venstre kant
for j in range(len(y[i])):
    highest_height=0
    for i in range(len(x)):
        højde = int((y[j])[i])
        if int((y[j])[i]) > highest_height:
            (booly[j])[i]=True
            highest_height = int((y[j])[i])


#Højre kant
for j in range(len(y[i])):
    highest_height=0
    for i in range(len(x)):
        a=len(x)-i-1
        højde = int((y[j])[a])
        if int((y[j])[a]) > highest_height:
            (booly[j])[a]=True
            highest_height = int((y[j])[a])


#tælle mængden af true's:
sum=0

for i in range(len(x)):
    for j in range(len(y[i])):
        if (booly[j])[i] == True:
            sum += 1
        viewsx.append(find_nummer(i,j))
    viewsy.append(viewsx)
    viewsx=[]

print(sum)

#Find highest value in viewsy
highest_value=0

for i in range(len(x)):
    for j in range(len(y[i])):
        if viewsy[j][i]>highest_value:
            highest_value=viewsy[j][i]
print(highest_value)
find_nummer(8,49)