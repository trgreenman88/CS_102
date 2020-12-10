#Trent Greenman
#Stacks Homework
#CS 102 Spring 2020

from stackprint import Stack

##under Function
##Takes 2 stacks and moves the first one under the second one. It preserves
##the first stack, but changes the second one to be the combination described
##above
##INPUTS: r,s, which are two stacks
##Prints: None
##Returns: s, the second second stack which was changed

def under(r,s):
    
    t = Stack()
    #Empties s and moves its contents to t
    for i in range(s.size()):
        item1 = s.pop()
        t.push(item1)
    length = r.size()

    #Empties r and moves its contents to t
    for i in range(length):
        item2 = r.pop()
        t.push(item2)

    #Empties t and moves all of its contents to s and the top part of its
    #contents to r
    for i in range(t.size()):
        item3 = t.pop()
        s.push(item3)
        #Some contents are being added to r
        if r.size()<length:
            r.push(item3)
            
    return s

#-------------------------------------------------------------------------------
   
def main():
    letters = "ABCDEFG"
    st1 = Stack()
    for c in letters:
        st1.push(c)

    moreletters = "RSTUVW"
    st2 = Stack()
    for c in moreletters:
        st2.push(c)
        
    st1 = under(st2, st1)
    print(st1, " =RSTUVWABCDEFG")

    print(st2, " = RSTUVW")


main()
