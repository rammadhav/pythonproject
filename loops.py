
def pattern_programs():
    for i in range(4):
        for j in range(4):
            print(j+1, end=" ")
        print()

    print()

    for i in range(6):
        for j in range(i):
            print(j+1, end=" ")
        print()

    print()

    for i in range(5):
        for j in range(5 - i):
            print(j + 1, end=" ")
        print()

    print()

    for i in range(5, 0, -1):
        for j in range(5, i, -1):
            print("", end=" ")
        for k in range(i):
            print(k+1, end=" ")
        print()

    print()

    for i in range(0, 6, 1):
        for j in range(i, 5, 1):
            print("", end=" ")
        for k in range(i):
            print(k+1, end=" ")
        print()

    print()

    for i in range(3, 6, 1):
        for j in range(i, 5, 1):
            print("", end=" ")
        for k in range(i):
            print(k+1, end=" ")
        print()
    for i in range(4, 2, -1):
        for j in range(5, i, -1):
            print("", end=" ")
        for k in range(i):
            print(k+1, end=" ")
        print()

    print()

    for i in range(5):
        for j in range(i-5, -1):
            print(" ", end=" ")
        for k in range(i+1):
            print(k+1, end=" ")
        print()

    print()

    for i in range(5):
        for j in range(i - 3, 1):
            print(" ", end=" ")
        for k in range(i+1):
            print(k+1, end=" ")
        print()
    for i in range(4, 0, -1):
        for j in range(i - 4, 1):
            print(" ", end=" ")
        for k in range(i):
            print(k+1, end=" ")
        print()
    print()

def fact_prog():
    num = int(input("enter the number: "))
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


pattern_programs()
fact_prog()