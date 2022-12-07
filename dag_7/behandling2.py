indent_counter=0
i=0

f = open("output2.txt", "w")


with open("output.txt") as input2:
    for num, line in enumerate(input2, 1):
        if (line.find("-")!=-1):
            f.write("")
        elif (line.find("Replace")!=-1):
            f.write(line.split("cd")[1])
        else:
            f.write(line)

#with open("output.txt") as input2:
#    for line in lines:
#        if (line.find("with value")!=-1):
#            value=line.split("value: ")[1]
#            #get line number of line with value
#            linenumber=lines.index(line)
#
 #           templine=""
  #          input2.find("---¢")
#
 #   output2 = input2.readlines()

