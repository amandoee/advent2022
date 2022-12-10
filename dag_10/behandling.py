execution = []
register = []
current_execution=[]

signal = []
counter=1

tekst=[[],[],[],[],[]]

def addx(V):
    execution.append(0)
    execution.append(V)


with open("input.txt") as input2:
    for line in input2:
        if line.find("addx")!=-1:
            value=int(line[4:len(line)-1])
            addx(value)
        else:
            execution.append(0)

sum=1

counter2=0
for i in execution:
    if counter2==200:
        print("")
    register.append(i+sum)
    sum+=i
    counter2+=1

last_executed=0
for i in execution:
    if i != 0:
        current_execution.append(i)
        last_executed=i
    else:
        current_execution.append(last_executed)


counter=0
x=0
faktor=0
for i in register:
    #placement er registervrdien.
    if counter==40 or counter==80 or counter==120 or counter==160 or counter==200 or counter==240:
        x+=1
        faktor+=1
        print(" ")
    if counter==0 or (counter== register[counter-1]+40*faktor or counter==register[counter-1]-1+40*faktor or counter==register[counter-1]+1+40*faktor):
        #tekst[x].append("#")
        print("█",end="")
    else:
        #tekst[x].append(".")
        print(" ",end="")
    counter+=1


counter=1
for i in register:
    signal.append(i*(counter+1))


    counter+=1

print(" ")
print("The sums are: ",signal[20-2],signal[60-2],signal[100-2],signal[140-2],signal[180-2],signal[220-2])
print("The total being: ",signal[20-2]+signal[60-2]+signal[100-2]+signal[140-2]+signal[180-2]+signal[220-2])