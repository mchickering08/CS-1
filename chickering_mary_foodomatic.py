import random #imports random from library

foods = ["cauliflower", "tilapia fillet", "pork lion", "green beans", "rainbow carrots", "potatoes", "three color squash", "eggplant", "eye round of beef", "baguette"] #creates list
toppings = ["with balsamico", "with garlic and olive oil", "with minted yogurt", "soup", "chutney", "salad", "with salsa", "over sticky rice", "au jus", "with bamati rice"] #creates list
drinks = ["coke", "sprite", "lemonade", "water", "slushie", "fanta"] #creates list
food_prices = [7, 9, 10, 20, 13, 18, 7, 8, 10, 22] #food prices list
drink_prices = [2, 2, 3, 1, 4, 2] #drink prices list

total_cost = 0 #starting total cost at 0

while True: #infinate loop
    would_you_like_food = input("Hi! Welcome to food-o-matic. Would you like to order some food today?") #creates an imput for the player to answer if they want food

    if would_you_like_food == "no": #if user says no to food
        break #manually ends while true loop
    elif would_you_like_food == "yes": #complete the following if the player wants food 
        while True: #infinate loop
            try: #attempting to run following code
                number_of_items = int(input("How many items do you want?")) #creates an input for the number of food items the player wants

                if number_of_items <= 0: #complete following if the user's number is less than or equal to zero
                    print("Please enter a number greater than zero") #prints the text
                else: #otherwise
                    break #manually ends while true loop
            except ValueError: #if there's an error in the above code
                print("Enter an integer!") #prints the text that is a message to the user about the error
        for i in range(number_of_items): #for the amount that the player answered, the following items will print
            food = random.choice(foods) #randomly selecting food
            food_price = food_prices[foods.index(food)] #finding corresponding price for the food that was selected
            print(f"{food} {random.choice(toppings)}. Your price for this item ${food_price}") #prints the number above for food and toppings randomly
            total_cost += food_price #adds food price to total price
        break #manually ends while true loop
    else: #otherwise
        print("Invalid") #prints the text

drink_option = input("Would you like a drink?") #creates an input for the player to answer if they want a drink

if drink_option == "yes": #complete the following if they say yes
    while True: #infinate loop
        try: #attempting to run following code
            drink_number = int(input("How many drinks do you want?")) #creates an input for the number of drink items the player wants
            break #manually ends while true loop
        except ValueError: #if there's an error in the above
            print("Enter an integer!") #prints message to user

    for i in range(drink_number): #for the amount that the player answered, the following items will print
        drink = random.choice(drinks) #randomly selects drink
        drink_price = drink_prices[drinks.index(drink)] #finding corresponding  price for drink that was selected
        print(f"Your drink is {drink}, which will cost you ${drink_price}") #prints the amount of drinks they wanted randomly
        total_cost += drink_price #adds drink price to total cost
elif drink_option == "no": #if they don't want a drink, will do following
    print("Okay, have a nice day") #prints the text

print(f"Your total cost is ${total_cost}")#prints total cost    
print("Have a nice day!")#prints the text
