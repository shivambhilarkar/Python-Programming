from functools import reduce


# Map Function
# Filter Function
# Reduce Function
# Join Function
# Lambda Function


# -- map function
def get_square(n) -> int:
    return n * n


def map_function_in_python():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    squared_numbers = map(get_square, numbers)
    print(squared_numbers)

    squared_numbers_list = list(map(get_square, numbers))
    print(f"Squared Numbers : {squared_numbers_list}")


# -- filter function
def is_number_even(number) -> bool:
    return number % 2 == 0


def filter_function_in_python():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter(is_number_even, numbers)
    print(even_numbers)

    even_numbers_list = list(filter(is_number_even, numbers))
    print(f"Number list : {even_numbers_list}")


# -- reduce function
def get_sum(num1, num2) -> int:
    return num1 + num2


def reduce_function_in_python():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = reduce(get_sum, numbers)
    print(f"Result : {result}")


# -- join function
def join_function_in_python():
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    template = " > "
    result = template.join(week_days)
    print(f"Week Days : {result}")


# -- lambda function
get_square_number = lambda number: number * number


def lambda_function_in_python():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for number in numbers:
        print(f" {get_square_number(number)}", end="")


if __name__ == "__main__":
    # map_function_in_python()
    # filter_function_in_python()
    # reduce_function_in_python()
    # join_function_in_python()
    lambda_function_in_python()
