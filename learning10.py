# learning10.py

''' create a script
that merges the three
text files into a new
text file containing
the text of all three
files. The filename
of the merged text
file should contain
the current timestamp
down to the millisecond
level. E.g.
"2016-06-01-13-57-39-170965.txt". '''

import glob2
import datetime
import time

filenames=glob2.glob("*.txt")

# create timestamps
# loop
# create new file with filename that is "now" as a string.

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w') as file:
    #open that file and then
    for filename in filenames:
        # for each entry in filenames, open that file...
        with open(filename,"r") as f:
            # read the data
            # write the data
            # or should it just be append the data?
            # the file is known as f.
            # read F and write it.
            # everything in the section above is done in file "#TIMESTAMP"
            
            # apparently the solution is: 
            file.write((f.read)+" \n") 
    file.write("done.")
    print("finished!")
# open file1,2,3
#append text of file1,2,3
#save filename as timestamps
