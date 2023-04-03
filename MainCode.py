# Code used to program Smart Lights, as well as
# to see if lights are on or off.
# Importing the time Module for Time checks.
import time

print("Please use Military Time Format (e.g. HH:MM, HH = 01-23, MM = 01-59)"
      )  # To explain Time Format. HH = Hour, MM = Minutes.
print("When Should Lights Turn On?: ")
When_on_Hr = int(input("HH: "))
When_on_Mn = int(input("MM: "))

print("\nWhen Should Lights Turn Off?: ")
When_off_Hr = int(input("HH: "))
When_off_Mn = int(input("MM: "))

# To combine the chosen Hour and Minutes of the
# Start and End times so that they are together
# to disply a proper Time Format.
star_tim = str(f"{When_on_Hr}:{When_on_Mn}")
end_tim = str(f"{When_off_Hr}:{When_off_Mn}")

# Variable to check that entered time is in range
# of a correct Military Time Format.
chk_tim = When_off_Mn == When_off_Mn >= 0 and When_off_Mn <= 59 and When_off_Hr <= 23 and When_off_Hr >= 0 and When_on_Mn == When_on_Mn >= 0 and When_on_Mn <= 59 and When_on_Hr <= 23 and When_on_Hr >= 0

# Most possible ways the answer No could be entered.
# Maybe an easier or more effective way to do this,
# but at the time I could not think of one.
pos_ans = [
  "No", "nO", "no", "N0", "n0", "No ", "nO ", "no ", "N0 ", "n0 ", " No",
  " nO", " no", " N0", " n0", " No ", " nO ", " no ", " N0 ", " n0 "
]

# Line 47 imports functions from the time Module so
# that the local time could display in a "readable"
# format.
# Line 50 checks if the loc_tim is in range of the
# Start and End times chosen by the user.
if chk_tim:
  print(
    f"\nLight Schedule: {When_on_Hr}:{When_on_Mn} TO {When_off_Hr}:{When_off_Mn}"
  )
  print("\nPlease type Yes or No:")
  Question = input("Check if Lights are ON?: ")
  if Question not in pos_ans:
    print("\nCurrent Local Time: ")
    from time import gmtime, strftime, localtime
    loc_tim = strftime("%H:%M", localtime())
    print(loc_tim)
    if loc_tim >= star_tim and loc_tim < end_tim:
      print("\nYour Lights are ON!")
    else:
      print("\nYour Lights are OFF!")
  else:
    print("\nThank You, Have a Good Day!")
else:
  print("\nPlease Try Again, Wrong Time Format Used!")
