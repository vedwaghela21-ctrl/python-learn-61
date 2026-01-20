def greet():
    print("hi!!! hello world")


def getNumber():
    number = int(input("Enter a number: "))
    return number


def checkOddEven(num):
    return num % 2 != 0   # True if odd, False if even


def main():
    greet()
    number = getNumber()

    if checkOddEven(number):
        print("{} is odd.".format(number))
    else:
        print(f"{number} is even")


if __name__ == "__main__":
    main()
