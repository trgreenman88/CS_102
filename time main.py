from TimeTRG import Time
####
## INSERT YOUR TIME CLASS HERE TO TEST




def main():
    time0 = Time()
    print( time0 ) # prints: 0 hours, 0 minutes
    time1 = Time(6)
    print( time1 ) # prints: 6 hours, 0 minutes
    time2 = Time(3, 30)
    print( time2 ) # prints: 3 hours, 30 minutes
    time3 = Time(30, 75)
    print( time3 ) # prints: 31 hours, 15 minutes
    time4 = Time(3.5)
    print( time4 ) # prints: 3 hours, 30 minutes
    print( time3 + time4 ) # prints: 34 hours, 45 minutes
    print( time3 ) # still prints: 1 hours, 15 minutes
    print( time1 + 10 ) # prints: 16 hours, 0 minutes
    print( 0.75 + time2 ) # prints: 4 hours, 15 minutes

main()
