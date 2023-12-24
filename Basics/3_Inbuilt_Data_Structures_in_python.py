# In build data structures -> List, Tuple, Set, Dictionary

if __name__ == "__main__":
    print("script started")

    # List -> leaner data structure
    list = []  # list initialization
    for num in range(1, 10):
        list.append(num)
    print(f"List : {list}")

    # Tuple  -> unmodifiable object
    tuple = (1, "tom", "cruise")
    print(f"Tuple : {tuple}")

    # Set -> store unique elements
    set = {1, 2, 3, 4, 5, 5, 5, 6, 7}
    print(f"Set : {set}")

    # Dictionary -> store key:value pair
    dictionary = {1: "Monday", 2: "Sunday"}
    print(f"Dictionary : {dictionary}")
    print(dictionary.get(1))
    print(dictionary.get(2))
    print(dictionary.get(3))
