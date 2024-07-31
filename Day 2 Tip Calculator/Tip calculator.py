#Data Types
print("Welcome to the chip calculator!")
Totalbill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("how many peopleto split the bill?"))
tip_as_percent = tip / 100
bill = Totalbill + Totalbill * tip_as_percent
Eachperson = round(bill / people, 2)
duplicate = "{:.2f}".format(bill)
print("Each person should pay: " + duplicate)
