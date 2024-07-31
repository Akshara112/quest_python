#to print an equilateral triangle of n lines
n = int(input('enter the side of the equilateral triangle'))
k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(end = " ")
    k -= 1
    for j in range(0, i + 1):
        print("* ", end='')
    print("\n")


