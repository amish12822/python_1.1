"Grade students based on marks"

marks = int(input("Enter your total marks: "))

if (marks >= 90):
    print("Grade: A")
elif(marks < 90 and marks >=80):
    print("Grade: B")
elif(marks <80 and marks >= 70):
    print("Grade: C")
else:
    print("Grade: D")
