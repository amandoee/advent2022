import re

command = "$"
command_indent = "---"
file_indent = "   "
counter = 0
last_command = ""
dir_line_number_to_replace=0
f = open("output.txt", "a")

# array for file directories
file_dir = []
parent=""

#Function to write line to file


# sum files in directory and subdirectories
def find_sum(linje):
    sum = 0
    if linje.find(command) == -1:
        sum = int((re.findall(r'\d+', linje))[0])
        return sum
    else:
        return 0

directorysum=0
latest_directory=""

with open("input.txt") as input2:
    for num, line in enumerate(input2, 1):

        if line.find(command) != -1:
            if ((line.find("cd")!= -1) and (line.find("cd ..")==-1)):
                
                #Her går man IND i et directory.
                latest_directory=line

                last_command="cd x"
                print(counter*command_indent, line, end="")
                f.write(counter*command_indent + line)
                counter+=1


            elif ((line.find("cd")!=-1) and (line.find("cd ..")!=-1)):
                
                #Her går man tilbage. Hvis ls var det sidste der blev kørt, så er det en hel directory sum
                if last_command=="ls":
                    #print(counter*file_indent,directorysum,"<-- SUM OF DIRECTORY",latest_directory,end="")
                    #print("REPLACE ",latest_directory," WITH VALUE: ",directorysum,end="")
                    f.write("-Replace "+latest_directory+" with value: "+str(directorysum)+"\n")
                    #print(directorysum,"\n")
                    directorysum=0

                if last_command=="cd ..":
                    


                last_command="cd .."
                print(counter*command_indent, line, end="")
                f.write(counter*command_indent+line)
                counter-=1
            
            else:
                print(counter*command_indent, line, end="")
                f.write(counter*command_indent + line)

                if line.find("ls")!=-1:
                    last_command="ls"
                
        elif line.find(command) == -1:
            print(counter*file_indent,line,end="")
            f.write(counter*file_indent + line)


            if (line.find("dir")!=-1):
                last_command="dir"

            if last_command=="ls" and line.find("dir")==-1:
                directorysum+=find_sum(line)
        
#print file_dir as directory tree like above


#Function that copies input.txt to input_v2.txt

#Gå fra 0 til linjenummeret hvor "dir directory_navn" står. Erstat med en talværdi, og slet alt mellem MEDMINDRE det er andre filer/directories.
