days = int(input("How many days did you use the car: "))
km = float(input("How many km did you drive: "))
paid = days * 60 + (km * 0.15)
print("The total amount you have to pay for renting the car is {:2}".format(paid))
