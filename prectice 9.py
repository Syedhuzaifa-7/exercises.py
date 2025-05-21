marks = [3, 4, 6,9,7]
names = ["ali", "hamza", "hashim"]
print(marks[-4])
print(marks[len(marks)-3])
print(marks[2-3])
print(marks[2])
if 3 in marks :
    print("yes")
else :
    print("no")
print(marks[1:3:4])
print(marks[1:3])
print(marks[0:len(marks)])
print(marks[:])
print(marks[:4])
marks[2] = 10
print(marks[:])
marks + names 
print(marks + names)
del(names[2])
print(names) 