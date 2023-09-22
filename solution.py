#NOTE:There are many solutions to complete this exercise. Here is one of those solutions

# .................................code here..............................
# Get weather input from user
weather = input("Is it rainy, sunny, or cold today? ").lower()

# Recommend outfit based on weather using conditional statements
if weather == "rainy":
    print("It's best to wear a raincoat and carry an umbrella.")
elif weather == "sunny":
    print("Wear your favorite t-shirt and sunglasses!")
elif weather == "cold":
    print("Don't forget a heavy jacket and a scarf.")
else:
    print("Sorry, I don't have an outfit recommendation for that weather condition.")
    
    # ...........................code above...............................