
print("Enter 'q' to quit.")
while True:
    reason = input("Why do you like programming? ")
    if reason.lower() == 'q':
        break
    with open("programming_poll.txt", "a") as file:
        print(file.read())
        file.write(f"{reason}\n")

