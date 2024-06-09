# EXAMPLE 5: Ask the user how many minutes they exercise daily and provide health advice (be creative!).
exercise = int(input("How many minutes do you exercise daily? "))
if exercise >= 60:
    print("You are doing great! Keep it up!")       
elif exercise >= 30:
    print("You are doing good! Try to increase your workout time")
else:
    print("You need to exercise more! Aim for at least 30 minutes a day")