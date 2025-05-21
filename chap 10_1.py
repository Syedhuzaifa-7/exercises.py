filename = "guest.txt"

# Read the entire file
with open(filename) as file:
    contents = file.read()
print("=== Read entire file ===")
print(f'Content is {contents}')

# Loop over the file object
print("\n=== Loop over file object ===")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# Store lines in a list and work outside the with block
print("\n=== Read lines into a list ===")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
 