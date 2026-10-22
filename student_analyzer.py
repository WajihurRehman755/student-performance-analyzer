marks = {}

for i in range(1, 4):
    subject = input("Enter Subject name: ")

    while subject == "":
        print("Subject name cannot be empty.")
        subject = input("Enter Subject name: ")

    while subject in marks:
        print("Subject already exists. Enter a different subject.")
        subject = input("Enter Subject name: ")

        while subject == "":
            print("Subject name cannot be empty.")
            subject = input("Enter Subject name: ")

    valid = False

    while valid == False:
        try:
            mark = int(input("Enter marks: "))
            if 0 <= mark <= 100:
                valid = True
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid marks. Please enter a number.")

    marks[subject] = mark

total = 0

for subject, mark in marks.items():
    total += mark

maximum = 300
percentage = total / maximum * 100
print("Total Marks:", total, "/", maximum)
print("\n--- Student Performance Report ---")
print(round(percentage, 2), "Percent")

average = total / len(marks)
print(round(average, 2), "Average Marks")

print("\n--- Subject Performance ---")

highest = max(marks.values())

for subject, mark in marks.items():
    if highest == mark:
        print(subject, "Highest Marks", highest)

lowest = min(marks.values())

for subject, mark in marks.items():
    if lowest == mark:
        print(subject, "Lowest Marks", lowest)

print("\n--- Final Grade ---")

if percentage >= 96:
    grade = "A++"
elif percentage >= 91:
    grade = "A+"
elif percentage >= 86:
    grade = "A"
elif percentage >= 81:
    grade = "B++"
elif percentage >= 76:
    grade = "B+"
elif percentage >= 71:
    grade = "B"
elif percentage >= 61:
    grade = "C+"
elif percentage >= 51:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "U"

print("Grade:", grade)
