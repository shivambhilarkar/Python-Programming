# Range statements
# Loops -> for each, while loop
# Conditional statements -> if else, if elif


def range_in_python():
    # range statements create input with specific range
    numbers = range(1, 10)
    print(numbers)
    # for loop
    for num in numbers:
        print(num, end=' ')
    print()

    # range with steps
    even_numbers = range(0, 10, 2)
    for num in even_numbers:
        print(num, end=' ')
    print()

    # for loop with range
    for num in range(1, 10):
        print(num, end=' ')
    print()


# if else statement
def condition_statements():
    day = str(input("Enter Day : "))
    if day.upper() == "SUNDAY":
        print("It's Holiday")
    elif day.upper() == "SATURDAY":
        print("It's Weekend")
    else:
        print("It's Workday")


# while loop
def while_loop():
    number = int(input("Enter Number : "))
    while number >= 0:
        print(number, end=' ')
        number -= 1
    print()


if __name__ == "__main__":
    print("script started")

    # range_in_python()
    # condition_statements()
    while_loop()
