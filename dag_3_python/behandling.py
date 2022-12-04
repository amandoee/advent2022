sum=0
sum2=0
found=0
counter=0


with open("../dag_3/input.txt") as input:
    data = [i for i in input.read().strip().split("\n")]

    for item in data:
        half1=slice(0,len(item)//2)
        half2=slice(len(item)//2,len(item))

        for element in item[half1]:
            if element in item[half2] and found==0:
                if (element.isupper()==True):
                    sum+=ord(item[(item.find(element))].lower())-96+26
                else:
                    sum+=ord(item[(item.find(element))])-96
                found=1
                test = element.isupper
        found=0
    print(sum)
    print(data)
    #MANGLER DEL 2. BØR VÆRE NEMT NOK
