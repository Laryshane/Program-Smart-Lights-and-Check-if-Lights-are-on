# Code used to program Smart Lights, as well as to see if lights are on or off.

print("Please use Military Time Format (e.g. HH.MM, HH = 01-24, MM = 01-59)"
      )  # To explain Time Format.

When_on = float(input("When Should Lights Turn On?: "))

When_off = float(input("\nWhen Should Lights Turn Off?: "))

# LINE 10 is To make sure user can't enter an input less than 00.01 or higher than 24.00.
# LINE 13 is used to have user enter only Yes or No exactly.
# LINE 16 are all the ways "No" could be entered.
# LINE 22 is the same reason as LINE 10.
# LINE 23 is if User breaks time rule in LINE 20.
# LINE 31 is if user breaks time ruin in LINE 15.
if When_off == When_off > 00.01 and When_off <= 24.00 and When_on == When_on > 00.01 and When_on <= 24.00:
  print(f"\nLight Schedule: {When_on} TO {When_off}")
  print("\nPlease type Yes or No:")
  Question = input("Check if Lights are ON?: ")
  if Question not in ["No", "nO", "no", "N0", "n0"]:
    print("\nPlease use Military Time Format (e.g. HH.MM, HH = 01-24, MM = 01-59)")
    Wht_time = float(input("What Time is it?: "))
    if Wht_time > When_on and Wht_time < When_off:
      print("\nYour Lights are ON!")
    elif Wht_time < 00.01 or Wht_time > 24.00:
      print("\nPlease Try Again")
    else:
      print("\nYour Lights are OFF!")
  else:
    print("\nThank You, Have a Good Day!")
else:
  print("\nPlease Try Again!")
