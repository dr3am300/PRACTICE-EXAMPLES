# EXAMPLE 6: Recommend a type of coffee based on user preferences about sweetness and milk.  
type_of_milk = input("Do you like milk in your coffee? (yes, no): ")    
sweetness = input("Do you like your coffee sweet? (yes, no): ")
if type_of_milk == "yes" and sweetness == "yes":
    print("You should try a latte") 
elif type_of_milk == "yes" and sweetness == "no":
    print("You should try a cappuccino")
elif type_of_milk == "no" and sweetness == "yes":
    print("You should try a macchiato")
else:
    print("You should try a black coffee")