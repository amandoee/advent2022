class monkey:
    items = []
    operation = 0
    
    #pointer to the next node
    t=None
    f=None
    
number=0
monkeys=list()

with open("case_input.txt") as input2:
    for line in input2:
        monkeys.append(monkey())
        
        line=line.strip("\n").split(", ")
        monkeys[number].items=line
        number+=1
input2.close()

number=0
with open("case_operands.txt") as data:
    for line in data:
        line=line.split("\n")
        for i in range(len(line)):
            monkeys[number].operation=int(line[0])
        number+=1
data.close()

number=0
with open("case_relations.txt") as data2:
    for line in data2:
        line=line[0:line.find("\n")]
        line=line.split(" ")
        monkeys[number].t=int(line[0])
        monkeys[number].f=int(line[1])
        number+=1
data2.close()

monkey_inspections=[0,0,0,0,0,0,0,0]

for n in range(20):
    for i in range(len(monkeys)):
        monkey_inspections[i]+=len(monkeys[i].items)
        
        for item in monkeys[i].items[0:]:
            
            if i == 0:
                monkeys[i].items[0]=int(monkeys[i].items[0])*19
            elif i == 1:
                monkeys[i].items[0]=int(monkeys[i].items[0])+6
            elif i == 2:
                monkeys[i].items[0]=int(monkeys[i].items[0])*int(monkeys[i].items[0])
            elif i == 3:
                monkeys[i].items[0]=int(monkeys[i].items[0])+3
            elif i == 4:
                monkeys[i].items[0]=int(monkeys[i].items[0])*17
            elif i == 5:
                monkeys[i].items[0]=int(monkeys[i].items[0])+3
            elif i == 6:
                monkeys[i].items[0]=int(monkeys[i].items[0])*int(monkeys[i].items[0])
            elif i == 7:
                monkeys[i].items[0]=int(monkeys[i].items[0])+6


            
            if int(monkeys[i].items[0])%monkeys[i].operation==0:
                monkeys[monkeys[i].t].items.append(monkeys[i].items[0])
            else:
                monkeys[monkeys[i].f].items.append(monkeys[i].items[0])
            monkeys[i].items.pop(0)
    
    for items in monkeys:
        print("Round: ",n+1,"--",items.items)
