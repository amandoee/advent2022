sum1=0
sum2=0
def range_overlap(range1, range2):
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    if (x1>=y1 and x2<=y2) or (y1>=x1 and y2<=x2):
        return 2
    if x1 <= y2 and y1 <= x2:
        return 1
    else:
        return 0 

with open("input.txt") as input:
    data = [i for i in input.read().strip().split("\n")]
    for item in data:
        tal=item.replace(",","-")
        tal=tal.split("-")
        
        x=range(int(tal[0]),(int(tal[1])))
        y=range(int(tal[2]),int(tal[3]))

        if range_overlap(x,y)==2:
            sum1+=1
            sum2+=1
        elif range_overlap(x,y)==1:
            sum2+=1
    
    print(sum1)   
    print(sum2)