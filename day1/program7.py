
score=int(input("Enter the average score to check"))
if score>=0 and score<=49:
    print('fail')
elif score<=74:
    print('second class')
elif score<=90:
    print('first class')
elif score<=100:
    print('distinction')
else:
    print('invalid input')