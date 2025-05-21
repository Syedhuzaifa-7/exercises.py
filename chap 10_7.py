name = True

while name:
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")

    try:
        result = int(first) + int(second)
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(f"The sum is: {result}")

