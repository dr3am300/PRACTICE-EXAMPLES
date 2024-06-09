# You are programming a smart wardrobe assistant that suggests outfits to users based on the day's temperature and the type of event they are attending. 
# The wardrobe has the following recommendation criteria:
# • If the temperature is below 15°C and the event is "formal", suggest a "Warm formal suit".
# • If the temperature is below 15°C but the event is "casual", suggest a "Cozy sweater and jeans".
# • If the temperature is above 15°C and the event is "formal", suggest a "Light formal suit".
# • For any other combination, suggest a "T-shirt and shorts".

# task: 
# Write a Python program that:
# 1. Asks the user about the day's temperature in Celsius or Fahrenheit.
# 2. Asks the user about the type of event they are attending (formal/casual).
# 3. Determines the outfit based on the above criteria.
# 4. Displays the recommended outfit to the user.
# Hint: Use nested if statements to determine the outfit based on the day's temperature and the type of event.


temperature = float(input("Enter the day's temperature in Celsius or Fahrenheit: "))
event = input("Enter the type of event you are attending (formal/casual): ")

if temperature < 15 or temperature < 59:
    if event == "formal":
        print("Recommendation: Warm formal suit")
    elif event == "casual":
        print("Recommendation: Cozy sweater and jeans")
elif temperature > 15 or temperature > 59:
    if event == "formal":
        print("Recommendation: Light formal suit")
    else:
        print("Recommendation: T-shirt and shorts")
else:
    print("Recommendation: T-shirt and shorts")
    
    
        
