class Time:

    ## __init__ Method
    ## creates a time in hours and minutes where the minutes are a positive integer
    ## between 0 and 60 and the hour is another positive integer. mins and hrs have
    ## a default value of 0 in case the user doesn't enter a value
    
    def __init__(self,hrs=0,mins=0):
        self.hrs = hrs
        self.mins = mins

        #if hours is a float, convert the leftover decimals into minutes
        if self.hrs - int(self.hrs) != 0:
            self.mins += (self.hrs - int(self.hrs))*60
            
        #keeps minutes between 0 and 60
        while self.mins >= 60:
            self.hrs += 1
            self.mins -= 60
            
        #converts our hours and minutes to integers
        self.hrs = int(self.hrs)
        self.mins = int(self.mins)
        
#------------------------------------------------------------------------------------------            

    ## __str__ Method
    ## Converts the numbers we created with __init__ into a form that is easy to read.
    ## INPUTS: A time
    ## RETURNS: A time that is easy to read
        
    def __str__(self):
        return(str(self.hrs) + " hours and " + str(self.mins) + " minutes")
    
#-------------------------------------------------------------------------------------------

    ## __add__ Method
    ## First, converts the inputs to a Time if they aren't already and then adds the
    ## two times together. It also makes sure that the minutes stays between 0 and 60.
    ## INPUTS: A time and either another time of a number
    ## RETURNS: The sum of the two times
    
    def __add__(self,other):
        if type(self) == float or type(self) == int:
            self = Time(self)

        if type(other) == float or type(other) == int:
            other = Time(other)
            
        newhrs = self.hrs + other.hrs
        newmins = self.mins + other.mins

        #keeps minutes between 0 and 60
        while newmins >= 60:
            newhrs += 1
            newmins -= 60
        return Time(newhrs,newmins)
    
#-------------------------------------------------------------------------------------------

    ## __radd__ Method
    ## First, converts the inputs to a Time if they aren't already and then adds the
    ## two times together in reverse order. Doing this allows us to enter an number
    ## before the time when adding them together. It also makes sure that the minutes
    ## stays between 0 and 60. This is used only when __add__ doesn't work
    ## INPUTS: A number and time
    ## RETURNS: The sum of the two times
    
    def __radd__(self,other):
        if type(self) == float or type(self) == int:
            self = Time(self)
            
        if type(other) == float or type(other) == int:
            other = Time(other)
            
        newhrs = self.hrs + other.hrs
        newmins = self.mins + other.mins

        while newmins >= 60:
            newhrs += 1
            newmins -= 60
        return Time(newhrs,newmins)
    
#-------------------------------------------------------------------------------------------

## main function that tests all of the cases given in the assignment
"""def main():
    time0 = Time()
    print(time0)
    time1 = Time(6)
    print(time1)
    time2 = Time(3,30)
    print(time2)
    time3 = Time(30,75)
    print(time3)
    time4 = Time(3.5)
    print(time4)
    print(time3+time4)
    print(time3)
    print(time1+0.75)
    print(0.75+time2)
main()"""

        
            
