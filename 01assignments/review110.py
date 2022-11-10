skill = int(input("How good are you at remembering your code? Answer with a number between 1-10. 1 being perfect and 10 being not at all. "))

if skill == 1:
    print("You are ready by son. Go on and takest your quize")
elif skill <= 5:
    print("Your are pretty good but need some more work. Take the quiz with caution.")
elif skill <= 10:
    print("You need a little more practice. Be patient and your reward will be within your favor. ")
else:
    print("Huh")