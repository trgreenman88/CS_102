#Trent Greenman
#Dice Solitaire
#CS 102 Spring 2020
import random
def main():
    #Introduction and initialize variables
    print("Welcome to Dice Solitare! We play to 100. Good luck!")
    score = 0
    print("Your total score is",score)
    turntotal = 0
    turnnum = 0
    #Continue to play the game until a score of 100 is reached
    while score < 100:
        #Generates random number between 1 and 6 for each die
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print("You rolled a",d1,"and a",d2)
        #Your roll is recorded as turn and as you continue to risk
        #it, each turn is added to turntotal
        turn = d1+d2
        turntotal += turn
        #Use this whenever you don't bust on any given turn
        if turn != 2 and turn != 12 and turn != 7:
            print("your turn-points is:",turntotal)
            #RoH is an input that determines whether someone will risk
            #it or hold.
            RoH = ""
            #Run this loop until someone enters a valid input for RoH
            while RoH != "R" and RoH != "H":
                RoH = input("Would you like to Risk it or Hold? Enter R/H")
                #If someone holds, add one to their turn count and add the
                #turn points to the score.
                if RoH == "H":
                    turnnum += 1
                    score += turntotal
                    print("You Held")
                    #Propper grammar for singular and plural turn counts
                    if turnnum == 1:
                        print("Your score is",score,"after",turnnum,"turn")
                        print("")
                    else:
                        print("Your score is",score,"after",turnnum,"turns")
                        print("")
                    #Reset turn points to 0 after the hold
                    turntotal = 0
                elif RoH == "R":
                    print("Your Risked It!")
                #Asks for another input if R or H is not entered
                else:
                    print("Please enter either R or H")
        #Use this whenever you bust on any given turn
        else:
            #Resets turn points to 0 and adds one to your turn count
            turntotal = 0
            turnnum += 1
            print("your turn-points were reset to 0")
            #Propper grammar for singular and plural turn counts
            if turnnum == 1:
                print("Your score is",score,"after",turnnum,"turn")
                print("")
            else:
                print("Your score is",score,"after",turnnum,"turns")
                print("")
    #After you exit the while loop, that means your score is at least 100
    #This means you won and you are given praise by the program
    print("Congrats! You won! It took you",turnnum,"turns")
main()
        
    
