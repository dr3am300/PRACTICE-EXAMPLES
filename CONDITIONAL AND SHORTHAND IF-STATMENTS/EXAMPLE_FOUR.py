# You are programming a digital bouncer for an online game portal. 
# The portal has games that are only suitable for players aged 18 and above. 
# You need to ensure that players meet the age requirement before they can access these games. 
# The bouncer has the following criteria:
# • If the player's age is 18 or above, display "You can drive!".
# • If the player's age is below 18, display "Not yet!"

# Write a Python program that:
# • Asks the user for their age.
# • Determines if the user is old enough to access the games based on the above criteria.
# • Displays the appropriate message to the user.
# Hint: Use nested if statements to determine the message based on the user's age.

age = int(input("Enter your age: "))

print("You can drive!") if age >= 18 else print("Not yet!")

# another way to write the code

if age >= 18:
    print("You can drive!")
else:
    print("Not yet!")
