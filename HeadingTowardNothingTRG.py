#Trent Greenman
#Heading Toward Nothing?
#CS 102 Spring 2020
import random
import math
#See main Function for program description

##initial Function
##Asks for a list size and creates a list of that many random numbers
##all between 1 and 99. If the input is not a positive number and at least
##1, then it asks you to enter the number again
##INPUTS: None
##Prints: The input statement and any error statements that may follow
##RETURNS: The list of random numbers between 1 and 99

def initial():
    numslist = []
    #assumes size to be a string
    size = ""
    
    #Keeps asking for an input until a positive number is given
    while type(size) != int:
        #Error handling for when the user enters a string
        try:
            #Forces size to be a float
            size = float(input("How long would you like your list to be? "))
            #Converts size to int only if it is at least 1
            if size>=1:
                size = int(size)
            #Asks for a new number if if the user enters a number less than 1
            else:
                print("Please enter a number >= 1")
        #If the user enters a string, tell them it isn't a number and ask
        #for a new input
        except ValueError:
            print("That's not a number")

    #Creates a list of random numbers between 1 and 99 of length 'size'        
    for i in range(0,size):
        num = random.randint(1,99)
        numslist.append(num)
    return numslist
#-------------------------------------------------------------------------------------------

##update function
##Changes the list into a list of the numbers that are the absolute value of
##the difference between each number and the one next to it in the list
##INPUTS: The list of random numbers between 1 and 99
##Prints: Nothing
##RETURNS: The new list of the differences

def update(numslist):
    updated = []
    for i in range(len(numslist)):
        #Adds the absolute value of the the difference between each number and
        #the one next to it in the list
        updated.append(abs(numslist[i]-numslist[i-1]))
    return updated
#-------------------------------------------------------------------------------------------

##round Function
##Asks how many times the user would like to update the list by taking the
##differences and keeps track of how many times the list is updated
##INPUTS: The new list of the differences
##Prints: The input statement that asks the user how many rounds to execute
##RETURNS: The finished list after updating it as many times as the user
##tells it to and the number of times that the list was updated. If the list
##reaches all 0's, each subsequent update is not counted

def round(updated):
    #Initialize variables
    final = updated
    sumlist = 0
    #numround keeps track of how many rounds are used
    #Start and numround = 2 because we already updated the list once and we
    #want to count the last round when we get to all 0's.
    numround = 2
    rounds = int(input("How many rounds would you like to execute? "))
    
    for i in range(rounds):
        #Calls the function update to keep taking the differences of the items
        #in the list
        final = update(final)
        #Adds the items in the final list together to see if the sum is 0
        for i in final:
            sumlist += i
        #Keep counting the round if the list hasn't reached all zeros
        if sumlist != 0:
            numround += 1
            sumlist = 0
        """print(final)"""
    return final,numround
#-------------------------------------------------------------------------------------------

##finished Function
##Checks to see if the list has reached all 0's
##INPUTS: The finished list after updating it as many times as the user
##tells it to
##Prints: Nothing
##RETURNS: True if the list reached all 0's and False if it didn't

def finished(final):
    ZeroCheck = 0
    #Looks at each item in final and tests whether each item is 0
    for i in final:
        if i != 0:
            #If any items are not 0, add 1 to the variable, ZeroCheck
            ZeroCheck += 1
            
    if ZeroCheck > 0:
        return False
    else:
        return True
#-------------------------------------------------------------------------------------------
    
##main Function
##Runs all of the functions above and displays the information in a way
##that is easy to read
##INPUTS: None
##Prints: The inial list and the list after 1 update. If the list reached
##all 0's, it congradulates the user, reminds the user of their initial list,
##and tells them how many rounds it took to reach all zeros. Otherwise, it
##prints a message feeling bad for the user, reminds the user of the origional
##list, tells the user how many times the list was updated, and tells the user
##what their final list ended up being.

def main():
    print("Hello! This program allows you to find the absolute value of the \n"
          "differences between a random number between 1 and 100 in a list and the \n"
          "numbers next to it in the list. You can repeat this as many times as you \n"
          "would like. Try to see if you can make your list all zeros! Good luck :)")
    print("")
    #Calls all the functions and assigns their returned values into variables
    start = initial()
    print(start)
    updated = update(start)
    print(updated,"is your list after 1 update")
    final,rounds = round(updated)
    tf = finished(final)
    
    #Print this stuff if the list reached all 0's
    if tf == True:
        print("")
        print("Congrats! Your list reached all zeros!")
        print("Your origional list was:",start)
        print("You reached all zeros after",rounds,"rounds!")
        
    #Print this stuff if the list did not reach all 0's
    if tf == False:
        print("")
        print("Oh no! You didn't get all zeros :(")
        print("Your origional list was:",start)
        print("You attempted this",rounds-1,"times")
        print("The list you ended up with is:", final)
main()
    
