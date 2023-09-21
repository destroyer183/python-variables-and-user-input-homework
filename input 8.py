subject = input("What subject? ")
total_marks = int(input("What is the total marks on the test? "))
test_marks = int(input("How many marks did you get? "))

diff = 100 / total_marks
percentage = test_marks * diff

percentage = round(percentage, 1)

print("subject: " + subject)
print("Total number of marks on the test: " + str(total_marks))
print("Your test marks: " + str(test_marks))
print("You got " + str(percentage))