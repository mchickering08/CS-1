import random #imports random library
    
def print_entry(websites, usernames, passwords, i):
    '''
    Prints the website, username, and password titles with the inputs.
    Args:
        websites(string), usernames(string), passwords(string): The three different catagories than can have inputs

    Returns:
        string: The usernames, passwords, and websites all printed together

    Raises:
        None

    '''
    print(f'''\nweb sites: {websites[i]}
username: {usernames[i]}
password: {passwords[i]}''')
def createpass(websites, usernames, passwords):
    '''
    Lets the user input a website, username, and password.
    Args:
        websites(string), usernames(string), passwords(string): The three different catagories than can have inputs

    Returns:
        string: Adds the websites, usernames, and passwords to the lists to be printed

    Raises:
        None

    '''
    while True:
        websites.append(input("Enter a website: "))
        usernames.append(input("Enter a username: "))
        passwords.append(input("Enter a password: "))       
        stop_option = input("Would you like to stop?")
        
        if stop_option == "yes":
            break  

def main():
    '''
    Runs the password keeper
    Args:
        none

    Returns:
        Runs the password keeper

    Raises:
        None

    '''
    websites = [] #creates a list for websites
    usernames = [] #creates a list for usernames
    passwords = [] #creates a list for passwords

    while True: #creates infinate loop
        open_keeper = input("Open password keeper? (Yes or no)") #creates an input for the user if they want to open password keeper
        if open_keeper == "yes": #complete the following if the user inputs "yes". If the user says no it will ask again
            enter_password = input("Enter password") #asks the user to enter the password as an input
            if enter_password == "securepassword123": #if the password equals the quotations, do the following. If the user's password is not this it will ask again.
                print("Correct!") #print correct
                break #then break, and continue to the next code

    createpass(websites, usernames, passwords) #completes the createpass function
    
    while True: #creates infinate loop
        mode = input('''Which would you like: 
1. Print all 
2. Print specific 
3. Add more
4. Edit username
5. Edit password
6. Generate Secure Password
7. Stop''') #asks the user which mode they would like, and they enter an integer

        if mode == "1": #complete the following if the user enters 1
            for i in range(len(websites)): #for every website there is (how many inputs)
                print_entry(websites, usernames, passwords, i) #run the print_entry function
        elif mode == "2": #completes the following if the user enters 2
            name = input("Enter a website") #asks the user to input a website that they already named earlier
            
            if name in websites: #if the inputed website is already in the websites list
                print_entry(websites, usernames, passwords, websites.index(name)) #print the website, username, and password that go along with the inputed website
        elif mode == "3": #complete the following if the user enters 3
            createpass(websites, usernames, passwords) #complete the createpass function
        elif mode == "4": #complete the following if the user enters 4
            name = input("Enter a website ") #asks the user to input a website that they already named earlier
            
            if name in websites: #if the inputed website is already in the websites list
                usernames[websites.index(name)] = input("Enter a new username: ") #Go to the listed website and ask the user to enter a new username
                print_entry(websites, usernames, passwords, websites.index(name))         
        elif mode == "5":
            name = input("Enter a website")
            if name in websites:
                passwords[websites.index(name)] = input("Enter a new password: ")
                print_entry(websites, usernames, passwords, websites.index(name))
                            
        elif mode == "6":
            pwd = []
            digits = list("123456789")
            letters = "abcdefghijklmjnopqrstuvwxyz"
            spec_ch = list("!@$%^&*()~")
            for i in range(3):
                pwd.append(random.choice(digits))
                pwd.append(random.choice(list(letters.upper())))
                pwd.append(random.choice(list(letters)))
                pwd.append(random.choice(spec_ch))
            random.shuffle(pwd)
            string = ''.join(pwd)
            print(f"\n{string}\n")
        elif mode == "7":
            break
main()







