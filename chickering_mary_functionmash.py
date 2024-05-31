#**************************

#* Program: Function Mashup
#* Author: Mary Chickering
#* Date: 4/23/24
#* Teacher: Ms. Marciano

#**************************

import random #imports random library

def chorus(): #creates chorus function
    print("Our song is the slamming screen door") #prints a lyric inside the function
    print("Sneakin' out late, tapping on your window") #same as above
    print("When we're on the phone, and you talk real slow") #same as above
    print("'Cause it's late, and your mama don't know") #same as above
    print("Our song is the way you laugh") #same as above
    print("The first date, 'Man, I didn't kiss her, and I should have'") #same as above
    print("And when I got home, 'fore I said, 'Amen'") #same as above
    print("Asking God if he could play it again") #same as above
def sing(): #creates total song function
    print("I was ridin' shotgun with my hair undone") #prints lyric inside the function
    print("In the front seat of his car") #same as above
    print("He's got a one-hand feel on the steering wheel") #same as above
    print("The other on my heart") #same as above
    print("I look around, turn the radio down") #same as above
    print("He says, 'Baby, is something wrong?'") #same as above
    print("I say, 'Nothing, I was just thinkin' how we don't have a song'") #same as above
    print("And he says...") #same as above
    print("I was walkin' up the front porch steps after everything that day") #same as above
    print("Had gone all wrong and been trampled on") #same as above
    print("And lost and thrown away") #same as above
    print("Got to the hallway, well on my way to my lovin' bed") #same as above
    print("I almost didn't notice all the roses") #same as above
    print("And the note that said") #same as above
    chorus() #prints chorus function
    print("I've heard every album, listened to the radio") #prints lyric inside the function
    print("Waited for something to come along") #same as above
    print("That was as good as our song") #same as above
    chorus() #prints chorus function
    print("Oh, yeah") #prints lyric inside the function
    print("Oh, oh yeah") #same as above
    print("I was ridin' shotgun with my hair undone") #same as above
    print("In the front seat of his car") #same as above
    print("I grabbed a pen and an old napkin") #same as above
    print("And I wrote down our song") #same as above
def add(num1, num2): #creates a function with two variables (numbers)
    print("Number 1:", num1) #Prints the text which prompts the user to input a number, which will be stored in the num1 variable
    print("Number 2:", num1) #Prints the text which prompts the user to input the second number, which will be stored in the num2 variable
    print(num1 + num2) #adds the user's two numbers together and prints the sum
def print_list(list_to_print): #creates a function with one variable, a list
    for element in list_to_print: #for every element in the list, do the following
        print(element) #print each element
def contains_element(check_list, element): #creates a function that checks the list (variable) for an element (also a variable)
    if element in check_list: #if the element is in the checklist, do the following
        return True #return True to the user
    else: #otherwise (element is not in the list)
        return False #return False
def get_int(order): #creates a function that tests if the input is an integer
    while True: #while true loop
        try: #trys the following code, but doesn't fully run it
            number = int(input(f"Enter your {order} number: ")) #prompts the user to enter a number
            return number #returns the number
        except ValueError: #if there is a value error, prints the following
            print("Please enter an integer!") #prints text
def random_numbers(): #creates a function that prints a random number between two boundary numbers
    num1 = get_int("lower boundary") #prompts user for lower boundary number
    num2 = get_int("upper boundary") #promots user for upper boundary number
    print(random.randint(num1, num2)) #prints random integer between the two numbers
def replace_character(string, old_ch, new_ch): #creates a function that replaces letters in text
    new_string = "" #creates variable for new string
    for s in string: #creates for loop for variable in the string
        if s == old_ch: #if variable is in the old character complete the following
            new_string += new_ch #add the new character to the new string
        else: #otherwise
            new_string += s #keeps the string how it is
    return new_string #return the new string
def reversestring(text): #reverses the string
    return text[::-1] #returns the text, but reversed
def palindrome(string): #creates a funtion that checks if the string is a palidrome
    return reversestring(string) == string #returns the function if the string is equal to the revered string (used function from above)
def main(): #creeates a main function
    check_list = ["Pasta", "Pizza", "Salad"] #creates list
    text = "Hello World"[::-1] #creates variable that will be reversed
    element = "Pizza" #creates variable
    sing() #calls the sing function
    add(1, 2) #calls the add function, with the two variables
    foods = ["Pizza", "Pasta", "Chicken", "Salad"] #creates list
    print_list(foods) #calls the print list function with the food variable
    print(contains_element(check_list, element)) #prints the contains element function with two variables
    random_numbers() #calls random number function
    print(replace_character("hello world", "l","a")) #prints replace character with the origional phrase variable and replaced letters variables
    print(reversestring("bed")) #prints reverse string with variable
    print(palindrome("bed")) #prints palindrome string with variable
    print(palindrome("mom")) #prints palindrome string with variable (one that is a palidrome)

main()
