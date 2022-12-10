sum=0
max_sum=0
max_sum2=0
max_sum3=0

with open("input.txt") as input:
    data = [i for i in input.read().strip().split("\n")]
    for item in data:
        if item == '': 
            if sum>max_sum:
                max_sum2=max_sum
                max_sum=sum
            elif sum>max_sum2:
                max_sum3=max_sum2
                max_sum2=sum
            elif sum>max_sum3:
                max_sum3=sum
            sum=0
        else:
            sum+=int(item)
            
print("Den højeste sum af kalorier er:",max_sum)
print("Summen af de tre højeste mængder kalorier er: ",max_sum+max_sum2+max_sum3)