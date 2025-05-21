first = input("Enter the first number: ")
second = input("Enter the second number: ")

try:
    result = int(first) + int(second)
except ValueError:
    print("❌ You need to enter valid numbers.")
else:
    print(f"✅ The sum is: {result}")

