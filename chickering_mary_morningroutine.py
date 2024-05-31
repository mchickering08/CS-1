print("Alarm!")

while True:
    snooze = str.lower(input("Snooze?"))
    
    if snooze == "yes":
        print ("Go back to sleep for 10 more munutes")
    elif snooze == "no":
        print("Wake up!")
        break
    else:
        print("Invalid response")
        

while True:
    breakfast = input("Do you want breakfast?")
      
    if breakfast == "no":
        print ("You are hungry")
    elif breakfast == "yes":
        print ("You are full")
        break
    else:
        print("Invalid response")

while True:
    shower = input("Do you want to shower?")
      
    if shower == "no":
        print ("You stink")
    elif shower == "yes":
        print ("You are clean")
        break
    else:
        print("Invalid response")
        break
    
while True:
    brush = input("Do you want to brush your teeth?")
      
    if brush == "no":
        print ("Ew, you're gross")
    elif brush == "yes":
        print ("Thank god")
        break
    else:
        print("Invalid response")
        break
    
while True:
    school = input("Do you want to go to school?")
      
    if school == "no":
        print ("Your mom will be mad")
        break
    elif brush == "yes":
        print ("Go to the bus")
        break
    else:
        print("Invalid response")
        break

while True:
    bus = input("Do you want to take the bus?")
      
    if bus == "no":
        print ("You can't get to school")
    elif bus == "yes":
        print ("It just arrived")
        break
    else:
        print("Invalid response")
        break
    