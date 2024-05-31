#*Author: Chickering, Mary
#Date: 11/29/23
#Description: Play rock paper scissors with a bot. It keeps score and once someone gets to 10, they win the match.
#Bugs: None
#Challenges: str.lower, bot_score and user_score, score limit, option to stop game, user errors
#Sources: Ms. Marciano and Eli

import random #imports random library
import time #imports time module
import sys #imports system-specific parameters and functions.In this case it lets the program end itself later on
game = ["rock", "paper", "scissors"] #the list of weapons that can be chosen
bot_score = 0 #the bot score starts as 0
user_score = 0 #the bot score starts at 0

while True: #repeats block of code while it is true
    play = str.lower(input("Would you like to play? ")) #makes “play” an input and asks the user. Str.lower allows the user to type uppercase or lowercase and it would still work. It converts uppercase to lowercase



    if play == "no": #will complete the action (break) if the user inputs no
        Break #if the user says no, it will break the code
    elif play == "yes": #will complete action (playing the game) if user says yes
        print("Welcome to Rock, Paper, Scissors! Choose either rock, paper, or scissors, and try to beat me!") #will print this statement if the previous statement is true

        if user_score >= 10: #will complete the action if the user’s score is ten or above
            print("You win the match!") #will print this statement if the previous statement is true
            Break #breaks the code after it prints the statement
        elif bot_score >= 10: #will complete the action if the bot’s score is 10 or above
            print("You lose the match") #will print this statement if the previous statement is true
            Break #breaks the code after it prints the statement
        
        while True: #repeats the block of code while it is true
            user_weapon = str.lower(input("Enter stop to end. Rock, Paper, or Scissors?")) #makes “user_weapon” an input and asks the user. Str.lower allows the user to type uppercase or lowercase and it would still work. It converts uppercase to lowercase

            if user_weapon == "stop": #will complete the action if the user’s response is stop
                sys.exit() #stops the program if user says stop
            if user_weapon not in game: #will complete the action if the user inputs a weapon that is not in the list
                print("Invalid response") #prints the following
            Else: #will complete this action if nothing above is true
                bot_weapon = random.choice(game) #the bot will pick a random choice from the list
                print("I picked " + bot_weapon) #prints the bot’s random choice along with the phrase before

                if user_weapon == bot_weapon: #will complete the following action if the user’s input is the same as the bot’s random weapon
                    print("It's a tie!") #prints this phrase if above is true
                elif user_weapon == "rock" and bot_weapon == "scissors": #will complete the following action if the user’s input is rock and the bot’s weapon is scissors
                    print("You win!") #prints this phrase if the above is true
                    user_score += 1 #adds one point to the user score
                elif user_weapon == "rock" and bot_weapon == "paper": #will complete the following action if the user’s input is rock and the bot’s weapon is paper
                     print("You lose!") #prints this phrase if the above is true
                     bot_score += 1 #adds one point to bot’s score
                elif user_weapon == "scissors" and bot_weapon == "paper": #will complete the following action if the user’s input is is scissors and bot weapon is paper
                    print("You win!") #prints this phrase if the above is true
                    user_score += 1 #adds one point to the user’s score
                elif user_weapon == "scissors" and bot_weapon == "rock": #will complete the following action if the user’s input is scissors and amd the bots choice is rock
                    print("You lose!") #prints this phrase if the above is true
                    bot_score += 1 #adds one point to the bot’s score
                elif user_weapon == "paper" and bot_weapon == "scissors": #will complete the following action if the user’s input is paper and the bot’s input is scissors
                    print("You lose!") #prints this phrase if the above is true
                    bot_score += 1 #adds one point to the bot’s score
                elif user_weapon == "paper" and bot_weapon == "rock": #will complete the following action if the user’s input is paper and the bot’s input is rock
                    print("You win!!") #prints this phrase if the above is true
                    user_score += 1 #adds one point to the user’s score

                print("Bot score is",bot_score) #prints the bot’s score after every round
                print("User score is",user_score) #prints the user’s score after every round
    else: #completes the following action if none of the above is true
        print("Invalid") #prints this phrase

