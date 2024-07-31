from replit import clear
from art import logo

print(logo)


def highest_bid():
  maximum = 0
  nameofmaximumb = ""
  for key in bid_dict:
    if bid_dict[key] > maximum:
      maximum = bid_dict[key]
      nameofmaximumb = key
  print(f"The winner is {nameofmaximumb} with a bid of ${maximum}")


bid = True
bid_dict = {}
while bid:
  name = input("Enter the name:")
  bid_amount = int(input("enter the amount you want to bid:\n"))
  bid_dict[name] = bid_amount
  flag = input("want to bid again ? yes or no\n")
  if flag == "no":
    bid = False
    highest_bid()
