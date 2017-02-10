emails=['me@gmail.com','you@hotmail.com','they@gmail.com']

# for email in emails:
#     print(email)
print("this is a list of messages")


for email in emails:
    if 'gmail' in email:
        print(email)

planet=input("what planet are you from?")
print(planet)


def currency_converter(rate, euros):
    dollars=euros*rate
    return dollars
r=input("Enter rate: "))
e=input("Enter euros: "))
currency_converter(float(r),float(e))
print(dollars)
