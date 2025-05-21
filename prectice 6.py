password = "123"
for attempt in range(3):
    entered_password = input("Enter your password: ")
    if entered_password == password:
        print("Access granted!")
        break
    else:
        print(f"Incorrect password. Attempts remaining: {2 - attempt}")
else:
    print("Too many incorrect attempts. Account locked.")