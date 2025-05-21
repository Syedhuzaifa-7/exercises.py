
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Cannot find the file: {filename}")
    else:
        print(f"\nContents of {filename}:")
        print(contents)


