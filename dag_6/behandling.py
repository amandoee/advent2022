found=False
found2=False

def are_strings_different(strings, x):
  return len(set(strings)) == x

with open("input.txt") as input2:
    data = [i for i in input2.read().strip().split("\n")]
    for item in data:
        for a in range(3,len(item)):
                list =[item[a-3],item[a-2],item[a-1],item[a]]
                if (are_strings_different(list,4) and found==False):
                    print(list)
                    print(a+1)
                    found=True
        for a in range(13,len(item)):
                strings =[item[a-13],item[a-12],item[a-11],item[a-10],item[a-9],item[a-8],item[a-7],item[a-6],item[a-5],item[a-4],item[a-3],item[a-2],item[a-1],item[a]]
                if (are_strings_different(strings,13) and found2==False):
                    print(strings)
                    print(a+1)
                    found2=True