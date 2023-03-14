# Code used to program Smart Lights, as well as to see if lights are on or off.

print("Please use Military Time Format (e.g. HH.MM)") # To explain Time Format.
When_on = float(input("When Should Lights Turn On?: ")) # To get users desired time to turn lights on.

When_off = float(input("When Should Lights Turn Off?: ")) # To get users desired time to turn lights off.

print("Light Schedule:", When_on, "TO", When_off) # To show/confirm users Time Schedule.

print("Please type Yes or No") # To explain what input is needed for output.
Question = input("Check if Lights are ON?: ") # To get users input.

if Question in ["No","no","NO", "nO", "n0", "N0"]: # Different ways the input No could be typed.
  print("Thank you!") 
else:
  print("Please use Military Time Format (e.g. HH.MM)")
  Wht_time = float(input("What Time is it?: ")) # To get users current time.
  if Wht_time > When_on and Wht_time < When_off: # Users time needs to be greater than the scheduled start time but less than their scheduled end time.
    print("Lights are ON!") # Tell user their Lights are ON.
  else:
     print("Lights are OFF!") # Tell user their Lights are OFF.
