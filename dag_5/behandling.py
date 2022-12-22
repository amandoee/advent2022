list = []
counter=0
array=[]

def move(amount_to_move, fra, til):
    for i in range(amount_to_move):
        list[til-1].append(list[fra-1].pop())

def move_9001(amount_to_move, fra, til):
    for i in range(amount_to_move):
        #lav array med værdier der poppes
        array.append(list[fra-1].pop())

    for i in range(amount_to_move):
        #array reversed insert
        list[til-1].append(array.pop())

with open("stack.txt") as input2:
    data = [i for i in input2.read().strip().split("\n")]
    for item in data:
        item = item.split(",")
        list.append(item)

with open("input.txt") as input2:
    data = [i for i in input2.read().strip().split("\n")]

    valg = int(input("Del 1 eller 2: "))

    for item in data:
        item = item.split(" ")
        item2 = item
        print(item2)
        if valg==1:
            move(int(item[1]),int(item[3]),int(item[5]))
        else:
            move_9001(int(item[1]),int(item[3]),int(item[5]))

    answer=""
    for item in list:
        answer+=item[-1]
        print(answer)