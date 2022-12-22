execution = []
register = []
signal = []

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
for i in execution:
    register.append(i+sum)
    sum+=i



counter=0
faktor=0
for i in register:
    #placement er registervrdien.
    if counter==40 or counter==80 or counter==120 or counter==160 or counter==200 or counter==240:
        faktor+=1
        print(" ")
    if counter==0 or (counter== register[counter-1]+40*faktor or counter==register[counter-1]-1+40*faktor or counter==register[counter-1]+1+40*faktor):
        print("█",end="")
    else:
        print(" ",end="")
    counter+=1


counter=1
for i in register:
    signal.append(i*(counter+1))
    counter+=1

print(" ")
print("The sums are: ",signal[20-2],signal[60-2],signal[100-2],signal[140-2],signal[180-2],signal[220-2])
print("The total being: ",signal[20-2]+signal[60-2]+signal[100-2]+signal[140-2]+signal[180-2]+signal[220-2])