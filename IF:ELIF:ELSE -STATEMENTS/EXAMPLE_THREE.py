# EXAMPLE 3: Based on the temperature entered by the user, suggest an outfit to wear. Be creative!
temperature = int(input("Enter the temperature: "))

if temperature >= 80:
    print("Wear a tank top and shorts")
elif temperature >= 70:
    print("Wear a t-shirt and jeans")
elif temperature >= 60:
    print("Wear a light jacket and jeans")
else:
    print("Wear a heavy jacket and jeans its cold outside")