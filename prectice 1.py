percentage = int(input("Enter student percentage: "))

if percentage >= 1 and percentage <= 60:
    print("Your grade is 'F'")
elif percentage > 60 and percentage < 65:
    print("Your grade is 'C'")
elif percentage >= 65 and percentage < 70:  
    print("Your grade is 'C+'")
elif percentage >= 70 and percentage < 75:  
    print("Your grade is 'B'")
elif percentage >= 75 and percentage < 80: 
    print("Your grade is 'B+'")
elif percentage >= 80 and percentage < 85: 
    print("Your grade is 'A'")
elif percentage >= 85 and percentage <= 100:
    print("Your grade is 'A+'")
else:
    print("Student percentage is invalid")