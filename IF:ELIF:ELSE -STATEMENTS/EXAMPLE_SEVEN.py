# EXAMPLE 7: 

# You are tasked with creating a program for a library to calculate fines for overdue books The library has the following fine structure:
#    • $1 per day for books that are up to 5 days overdue.
#    • $2 per day for books that are 6 to 10 days overdue.
#    • $5 per day for books that are more than 10 days overdue.
# Write a Python program that:
# 1. Asks the user for the number of days a book is overdue.
# 2. Calculates the fine based on the above criteria.
# 3. Displays the fine amount to the user.

days_overdue = int(input("Enter the number of days the book is overdue: "))
fine = 0
if days_overdue <= 5:
    fine = days_overdue * 1
elif days_overdue <= 10:
    fine = days_overdue * 2
else:
    fine = days_overdue * 5

print(f"Your fine is ${fine}.")


