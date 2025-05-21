filename = "learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

print("\n=== Replacing 'Python' with 'C' ===")
for line in lines:
    print(line.replace("Python", "C").strip())


