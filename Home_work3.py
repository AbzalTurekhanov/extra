def basic_operations(a: int, b: int, selected_option: int) -> None:
    if selected_option == 1:
        print(f"answer a + b = {a + b}")
    elif selected_option == 2:
        print(f"answer a - b = {a - b}")
    elif selected_option == 3:
        print(f"answer a * b = {a * b}")
    elif selected_option == 4:
        print(f"answer a / b = {a / b}")
    elif selected_option == 5:
        print(f"answer a**b = {a ** b}")
    else:
        print("Invalid scenario, please, inform developer")


def factorial(a: int) -> None:
    res = 1
    for i in range(2, a + 1):
        res *= i
    print(f"answer a! = {res}")


def is_valid_number(num: str) -> bool:
    if num[0] == "-":
        return num[1:].isdigit()
    return num.isdigit()


def calculator() -> None:
    print("Available options:",
          "1. a + b",
          "2. a - b",
          "3. a * b",
          "4. a / b",
          "5. a**b(a to the b power)",
          "6. a!(factorial of a)",
          "7. exit",
          sep="\n")

    selected_option = input("Enter option: ")
    while not (selected_option.isdigit() and int(selected_option) in range(1, 8)):
        print("Please, enter valid option")
        selected_option = input("Enter option: ")
    selected_option = int(selected_option)

    if selected_option < 6:
        a = input("Insert a: ")
        while not is_valid_number(a):
            print("Please, insert valid a")
            a = input("Insert a: ")
        a = int(a)

        if selected_option == 4:
            b = input("Insert b: ")
            while not (is_valid_number(b) and int(b) != 0):
                print("Please, insert valid b")
                b = input("Insert b: ")
        else:
            b = input("Insert b: ")
            while not is_valid_number(b):
                print("Please, insert valid b")
                b = input("Insert b: ")
        b = int(b)
        basic_operations(a, b, selected_option)
    elif selected_option == 6:
        a = input("Insert a: ")
        while not (a.isdigit() and int(a) > 0):
            print("Please, insert valid a, a must be greater than 0")
            a = input("Insert a: ")
        a = int(a)
        factorial(a)
    if selected_option == 7:
        print("Finished")
        return
    return calculator()


calculator()
