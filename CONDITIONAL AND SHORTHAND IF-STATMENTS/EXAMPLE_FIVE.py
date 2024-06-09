# You are programming a digital menu for a modern cate that offers a variety of dishes catering to different dietary preferences. 
# The café wants to suggest dishes based on whether a customer prefers vegetarian or non-vegetarian meals and whether they want a sugar-free option. 
# The menu has the following recommendation criteria:
# • If the customer prefers a vegetarian meal and wants it sugar-free, suggest a "Fruit salad".
# • If the customer prefers a vegetarian meal but doesn't want it sugar-free, suggest a "Veg cake".
# • If the customer prefers a non-vegetarian meal and wants it sugar-free, suggest "Sugar-free ice cream".
# • For any other combination, suggest a "Chocolate brownie".

# Write a Python program that:
# • Asks the user about their meal type preference (veg/non-veg).
# • Asks the user about their dietary preference (sugar-free/regular).
# • Determines the dish based on the above criteria.
# • Displays the recommended dish to the user.
# Hint: Use nested if statements to determine the dish based on the user's meal type and dietary preference.

meal_type = input("Enter your meal type preference (veg/non-veg): ")
dietary_preference = input("Enter your dietary preference (sugar-free/regular): ")

if meal_type == "veg":
    if dietary_preference == "sugar-free":
        print("Fruit salad")
    else:
        print("Veg cake")
elif meal_type == "non-veg":
    if dietary_preference == "sugar-free":
        print("Sugar-free ice cream")
    else:
        print("Chocolate brownie")

# and that's it for this example!

print("Fruit salad") if meal_type == "veg" and dietary_preference == "sugar-free" else print("veg cake") if meal_type == "veg" else print("sugar-free ice cream") if dietary_preference == "sugar-free" else print("chocolate brownie")
    