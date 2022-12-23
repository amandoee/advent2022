
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
                    linje.append(1)
                elif letter=='E':
                    end=[num,line.index(letter)]
                    linje.append(26)

                else:
                    linje.append(char_to_number(letter))

            kort.append(linje)
            linje=[]
    
        return start, end, num+1, len(line), kort

start, end, height, width, kort = start_end_size()

travel_path=[]
last_action_reverse=[]
#function to move recursively
def useless(start):
    travel_path.append(start)
    #left
    if start[0]>0 and kort[start[1]][start[0]-1]!='.' and [start[0]-1,start[1]] not in travel_path and (kort[start[1]][start[0]]>= kort[start[1]][start[0]-1]-1):
            last_action_reverse.append("right")    
            useless([start[0]-1,start[1]])
    
    #up
    elif start[1]>0 and kort[start[1]-1][start[0]]!='.' and [start[0],start[1]-1] not in travel_path and (kort[start[1]][start[0]]>= kort[start[1]-1][start[0]]-1): #MANGLER ÆNDRING
            last_action_reverse.append("down")
            useless([start[0],start[1]-1])
    
    #right
    elif start[0]<width-1 and kort[start[1]][start[0]+1]!='.' and [start[0]+1,start[1]] not in travel_path and (kort[start[1]][start[0]]>= kort[start[1]][start[0]+1]-1):
            last_action_reverse.append("left")
            useless([start[0]+1,start[1]])
    
    #down
    elif start[1]<height-1 and kort[start[1]+1][start[0]]!='.' and [start[0],start[1]+1] not in travel_path and (kort[start[1]][start[0]]>= kort[start[1]+1][start[0]]+1): #MANGLER ÆNDRING
            last_action_reverse.append("up")
            useless([start[0],start[1]+1])
    
    #If no more moves are possible, paint the path as useless
    elif (start!=end):
        kort[start[1]][start[0]]='.'
        if (travel_path.pop()!=[0,0]):
            travel_path.pop()
        
        action=last_action_reverse.pop()
        #Nået hertil. Mangler backtracking funktion færddiggjort

        if (action=="left"):
            useless([start[0]-1,start[1]])
        elif (action=="right"):
            useless([start[0]+1,start[1]])
        elif (action=="up"):
            useless([start[0],start[1]-1])
        elif (action=="down"):
            useless([start[0],start[1]+1])


useless(start)

print(kort)

#Tilføj op og ned kritierier for at måtte hoppe. så bør det virke.

    