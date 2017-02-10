def f_to_c(f):
    if f<=-459.616:
        return "that doesn't make sense!"
    else:
        cels = (f-32)*5/9
        return cels



def c_to_f(c):
    if c <=-273.12:
        return "that doesnt make sense!"
    else:
        f = c*9/5+32
        return f

# print(f_to_c(-273.11))
# print(c_to_f(-273.12))

print("done.")

# printing the result of running a function on each item in an array
temperatures=[10, -20, -289, 100]
for i in temperatures:
    print(c_to_f(i))
