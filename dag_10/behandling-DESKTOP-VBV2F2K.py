execution = []
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

for i in execution:
    signal.append(i*execution[i])