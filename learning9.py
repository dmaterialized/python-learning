
# this script creates an empty file.
import datetime
filename=datetime.datetime.now()
now = datetime.datetime.now()
#create an empty file
def create_file():
# ''' this function creates an empty file '''
    with open(str(filename.strftime("%Y-%m-%d-%H-%M")),'w') as file:
        file.write("") # """ writing empty string """



now.strftime("%Y-%m-%d-%H-%M-%S-%f")

create_file()
