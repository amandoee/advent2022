monkey_handling =[0,0,0,0,0,0,0,0]
monkey_number=0
round=0

def push_monkey(monkey,num):
    round=0
    if monkey==0:
        monkey0(num,round)
    elif monkey==1:
        monkey1(num,round)
    elif monkey==2:
        monkey2(num,round)
    elif monkey==3:
        monkey3(num,round)
    elif monkey==4:
        monkey4(num,round)
    elif monkey==5:
        monkey5(num,round)
    elif monkey==6:
        monkey6(num,round)
    elif monkey==7:
        monkey7(num,round)
    else:
        print("Error: monkey not found")


def monkey0(num,round):
    num=num*13
    monkey_handling[0]+=1
    round+=1
    
    if round==22:
        return
    
    if (num%3==0):
        monkey2(num,round)
    else:
        monkey1(num,round)


def monkey1(num,round):
    num=num+2
    monkey_handling[1]+=1
    round+=1

    if round==22:
        return
    
    if (num%13==0):
        monkey7(num,round)
    else:
        monkey2(num,round)
    
    

def monkey2(num,round):
    num=num+8
    monkey_handling[2]+=1
    round+=1
    
    if round==22:
        return
    
    if (num%19==0):
        monkey4(num,round)
    else:
        monkey7(num,round)
    

def monkey3(num,round):
    num=num+1
    monkey_handling[3]+=1
    round+=1
    
    if round==22:
        return
    
    if (num%17==0):
        monkey6(num,round)
    else:
        monkey5(num,round)
    
    

def monkey4(num,round):
    num=num*17
    monkey_handling[4]+=1
    round+=1
    
    if round==22:
        return
    
    if (num%5==0):
        monkey6(num,round)
    else:
        monkey3(num,round)
    
    

def monkey5(num,round):
    num=num+3
    monkey_handling[5]+=1
    round+=1
    
    if round==22:
        return
    
    if (num%7==0):
        monkey1(num,round)
    else:
        monkey0(num,round)
    
    

def monkey6(num,round):
    num=num*num
    monkey_handling[6]+=1
    round+=1
    
    if round==22:
        return
    
    if (num%11==0):
        monkey5(num,round)
    else:
        monkey0(num,round)
    

def monkey7(num,round):
    num=num+6
    monkey_handling[7]+=1
    round+=1
    
    if round==22:
        return
    
    if (num%2==0):
        monkey4(num,round)
    else:
        monkey3(num,round)
    
    
with open("input_v2.txt") as data:
    for line in data:
        numre = line.strip("\n").split(", ")
        for num in numre:
            push_monkey(monkey_number,int(num))
        monkey_number+=1

print(monkey_handling)
print(139*130)


