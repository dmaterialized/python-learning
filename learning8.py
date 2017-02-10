# converts temp, prints to a file, tells user which line is being printed, resets on each run.
# quite sophisticated, for me.

import os
os.listdir()

# syntax demo
#print(f_to_c(-273.11))
#print(c_to_f(-273.12))

# what to do:::::::::::
# convert each item C to f
# create text file with values stored
# if value is lower than -273.15, do not write anything.

# ===========================================
def f_to_c(f):
    if f<=-459.616:
        return "that doesn't make sense!"
    else:
        cels = (f-32)*5/9
        return cels


def c_to_f(cels):
    if cels <=-273.12:
        return "that doesnt make sense!"
    else:
        f = cels*9/5+32
        return f


temperatures=[10,-20,-289,100,-233, 510]
print("hello")
print("the Writer is starting now.")
def theWriter(temperatures):
    with open('temps2.txt','w+') as file:
        file.write("===========\nThe Temperatures are:\n")
        for i in temperatures:
            if i>=-273.12:
                print("Wrote line: " +str(i))
                file.write(str(i)+"\n")
        file.write("all done.")
    print("finished task.")

# run everything
theWriter(temperatures)

# ===========================================


# for i in temperatures:
#     if i>=-273.12:
#         theTemp=i
#         print(c_to_f(theTemp))
#         # with open('temperatures.txt','a+') as file:
#             # file.write()

    #with open('temperatures.txt','a+') as file:
        # file.write(i)
        # print("wrote "+i+" lines")
