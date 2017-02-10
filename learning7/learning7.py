#files read and write

file=open('example.txt','r')
content=file.read() #set var to store file content
print(content) #prints file content
content=file.readlines() #var now contains lines
print(content)
#this doesn't work yet because
#we have already read the file (we aren't starting at 0)
# to fix this use seek.

file.seek(0)
content=file.readlines()
print(content) #this prints it, but has "\n" for newline

file.seek(0)
# content=[item.rstrip('\n') for item in content]

file.seek(0)
stripped=[i.rstrip('\n') for i in content]

print(stripped)

file.close()
# always close the file (this will save changes properly)

# write a new file
file=open("example2.txt",'w') # w mode instead of r mode to write a file
file.write("Line 1")
file.write("\nLine 2")
# how to execute this 20 times?
# use a for loop.

#first make an array
l=["Line 1","Line 2","Line 3", "Line 4"]
for item in l:
    file.write(item+"\n")
    print("wrote "+item+" line")
file.close()


# the other file handler methods are:
# r+ opens for read and write, file pointer placed at beginning.
#  w+ opens a file;
#       overwrites if file exists;
#       creates a new file if no file exists.
#  a opens a file for appending. pointer placed at the end of the file.
#  a+ opens for reading and appending. File pointer placed at end if
#       file exists. File opens in append mode.
#

#with statements
with open("example3.txt","a+") as file:
    file.seek(0)
    content=file.read()
    file.write("\nLine 6")
