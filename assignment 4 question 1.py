print("Q1")
while True:
    mark = int(input("Enter mark:"))
    if mark < 25:
        print("Grade: F")
    elif 25 <= mark < 45:
        print("Grade: E")
    elif 45 <= mark < 50:
        print("Grade: D")
    elif 50 <= mark < 60:
        print("Grade: C")
    elif 60 <= mark < 80:
        print("Grade: B")
    elif mark >= 80:
        print("Grade: A")
    user = input("Continue?(y/n)")
    if user == 'n':
        break