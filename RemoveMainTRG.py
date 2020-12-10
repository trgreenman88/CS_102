#Trent Greenman
#Stacks Homework
#CS 102 Spring 2020
from stackprint import Stack

##remove Function
##This takes a stack, s, and a data type that can be anything called target and it
##removes the first occurence of the target value in the stack, "first" meaning whichever
##is closer to the top of the stack
##INPUTS: s, a stack, and target, any value of any data type
##Prints: None
##RETURNS: The new stack with the target value removed

def remove(s,target):
    newstack = Stack()

    #Remove contents from the stack and put them in the holder (newstack)
    for i in range(s.size()):
        item = s.pop()
        if item != target:
            newstack.push(item)

        #if you reach a target character, reassemble s and return it
        else:
            for i in range(newstack.size()):
                item2 = newstack.pop()
                s.push(item2)
            return s
        
    #reassemble s and returns it if the target is not in the stack
    for i in range(newstack.size()):
        item3 = newstack.pop()
        s.push(item3)
    return s

#-------------------------------------------------------------------------------------------

def main():
    letters = "ABCDEFG"
    st = Stack()
    for c in letters:
        st.push(c)

    print(st)
    
    first = "D"
    st = remove(st, first)   #now st should be [ABCEFG)
    print("after first", st)  #cheating a bit - the stack is a list so we print it

    second = "H"
    st = remove(st, second)  #st should still be [ABCEFG)
    print("after second", st)

    third = "A"
    st = remove(st, third)
    print("after third", st)
main()
