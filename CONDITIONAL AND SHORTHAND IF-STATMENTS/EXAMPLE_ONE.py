# You are developing a feature for a movie streaming platform that suggests a movie genre to users based on their current mood and the day's weather. 
# The platform has the following recommendation criteria:
# • If the user is feeling "happy" and the weather is "sunny", recommend a "Comedy".
# • If the user is feeling "happy" but the weather is not "sunny", recommend a "Romantic" movie.
# • If the user is feeling "sad", recommend a "Drama".
# • For any other mood, recommend an "Adventure" movie.

# task: 
# Write a Python program that:
# 1. Asks the user about the day's temperature in Celsius.
# 2. Asks the user about the type of event they are attending (formal/casual).
# 3. Determines the outfit based on the above criteria.
# 4. Displays the recommended outfit to the user.
# Hint: Use nested if statements to determine the outfit based on the day's temperature and the type of event.

temperature = float(input("Enter the day's temperature in Celsius: "))
event = input("Enter the type of event you are attending (formal/casual): ")
feelings = input("Enter your current mood (happy/sad): ")

if feelings == "happy":
    if temperature > 20 and temperature < 30 and event == "casual" and feelings == "happy":
        print("Recommendation: Comedy movie") and print("Outfit: Casual")
    elif temperature > 20 and temperature < 30 and event == "formal" and feelings == "happy":
        print("Recommendation: Romantic movie") and print("Outfit: Formal")
    else:
        print("Recommendation: Adventure movie") and print("Outfit: Casual")
elif feelings == "sad":
    print("Recommendation: Drama movie") and print("Outfit: Casual")
else:
    print("Recommendation: Adventure movie") and print("Outfit: Casual")
    
# another way to write the code

if feelings == "happy":
    if temperature > 20 and temperature < 30:
        if event == "casual":
            print("Recommendation: Comedy movie") and print("Outfit: Casual")
        elif event == "formal":
            print("Recommendation: Romantic movie") and print("Outfit: Formal")
    else:
        print("Recommendation: Adventure movie") and print("Outfit: Casual")
elif feelings == "sad":
    print("Recommendation: Drama movie") and print("Outfit: Casual")
else:
    print("Recommendation: Adventure movie") and print("Outfit: Casual")
    
       
        