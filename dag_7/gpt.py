import re

command = "$"
command_indent = "---"
file_indent = "   "
counter = 0
last_command = ""
total_filesize = 0

with open("input.txt") as input2:
    for num, line in enumerate(input2, 1):
        if line.find(command) != -1:
            if ((line.find("cd")!= -1) and (line.find("cd ..")==-1)):
                last_command="cd x"
                print(counter*command_indent, line, end="")
                counter+=1
            elif ((line.find("cd")!=-1) and (line.find("cd ..")!=-1)):
                last_command="cd .."
                print(counter*command_indent, line, end="")
                counter-=1
            else:
                print(counter*command_indent, line, end="")
                
        elif line.find(command) == -1:
            # Extract the filesize from the line, if it exists
            filesize_match = re.search(r'\d+', line)
            if filesize_match:
                filesize = filesize_match.group()
            else:
                filesize = 0
            # Add the filesize to the total filesize for the current subdirectory
            total_filesize += int(filesize)
            # If the total filesize is greater than 100000, reset the total filesize and do not print the line
            if total_filesize > 100000:
                total_filesize = 0
            else:
                print(counter*file_indent,line,end="")
