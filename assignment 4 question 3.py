import random
#Answer to question 3 of assignment
for i in range(1,11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f'Question {i}:{a}x{b}='))
    if ans == a*b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a*b)