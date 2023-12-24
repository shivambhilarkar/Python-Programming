# Basic Input and Output Statements in python
# Function in python

# return type void
def print_hello_world():
    print("Hello world")


# return type int
def get_sum(num1, num2) -> int:
    return num1 + num2


# main function in python
if __name__ == "__main__":
    print("Script is started")

    #     take input in python - default type is string
    age = input("Enter Age : ")
    print(f"Age : {age} | Input Type : {type(age)}")

    #     cast input into specific data type - int() , float(), bool() etc.
    age = int(input("Enter Age : "))
    print(f"Age : {age} | Input Type : {type(age)}")

    # print statements
    print("Print and Enter cursor on new line,")
    print("hello world")

    print("Print and Stays cursor on same line,", end=' ')
    print("hello world")

    # functions in python
    print_hello_world()
    result = get_sum(10, 20)
    print(f"Sum : {result}")
