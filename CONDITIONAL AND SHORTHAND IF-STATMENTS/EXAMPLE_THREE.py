# A school offers various discounts to its students based on their academic performance and participation in extracurricular activities. 
# The discount criteria are as follows:
# • Students with a grade of 'A' and who are also part of the school's sports team get a 20% discount.
# • Students with a grade of A but not in the sports team get a 10% discount.
# • Students with a grade of 'B' and who are part of the school's drama club get a 15% discount.

# Write a Python program that:
# • Asks the user for their grade (A/B/C).
# • Asks if they are part of the sports team (yes/no).
# • Asks if they are part of the drama club (yes/no).
# • Determines the discount percentage based on the above criteria.
# • Displays the discount percentage to the user.
# Hint: Use nested if statements to determine the discount percentage based on the student's grade and extracurricular activities.

grade = input("Enter your grade (A/B/C): ")
sports_team = input("Are you part of the sports team? (yes/no): ")
drama_club = input("Are you part of the drama club? (yes/no): ")

if grade == 'A':
    if sports_team == 'yes':
        discount = 20
    else:
        discount = 10
elif grade == 'B':
    if drama_club == 'yes':
        discount = 15
else:
    discount = 0
print(f"Discount percentage: {discount}%")

        
    
    