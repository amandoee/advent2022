
def char_to_number(a):
    return (ord(a)-96)

#Find start and end
def start_end_size():
    with open("text_input.txt") as data:
        kort=[]
        linje=[]
        
        for num, line in enumerate(data):
            line=line.strip("\n")
            for letter in line:
                if letter=='S':
                    start=[num,line.index(letter)]
                    linje.append('S')
                elif letter=='E':
                    end=[num,line.index(letter)]
                    linje.append('E')

                else:
                    linje.append(char_to_number(letter))

            kort.append(linje)
            linje=[]
    
        return start, end, num+1, len(line), kort

start, end, height, width, kort = start_end_size()

for item in kort:
    print(item)
    