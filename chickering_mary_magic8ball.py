import random

while True:
    question = input("What do you want to ask the eight ball?")

    response = ["No","Yes","Definetly yes","Definetly no","Maybe"]

    if question == "stop":
        break
    elif "?" in question:
        print(random.choice(response)) 
    elif "Stop Program" in question:
        print("Program has stopped.")
        break
    else:
        print("Not a question")
