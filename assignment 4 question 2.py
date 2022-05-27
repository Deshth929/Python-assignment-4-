year = int(input('Enter year:'))
#Answer to question 2 of the assignment
if year % 4 == 0:
    if year % 100 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")
