from func import loginControl, pointControl
from lesson import Lesson

lessons = []
loginAttempt = 0
username = ""
surname = ""

miniBrace = "---------------------------------------"
brace = "======================================"

print("Turkis AI Hub - Homework");
print("Example name: Salih, surname: Gencer")

print(brace)

while loginAttempt < 3:
    
    username = str(input("Please write your name : "))
    surname = str(input("Please write your surname : "))

    if loginControl(username, surname):
        break
    else:
        print("Please try again.")
        loginAttempt += 1

if loginAttempt == 3:
    print("Please try again later!")
    exit()
else:
    print(f"Welcome {username} {surname}")

print(brace)

addedLessons = 0
while addedLessons < 5:
    
    if addedLessons > 2:
        print("You have added at least 3 lessons. You can press the letter q to exit.")
    else:
        print("You must add at least 3 courses.")
    
    lessonName = str(input("Please add a lesson: ")).strip()
    
    print(miniBrace)

    if lessonName == "q":
        break

    lessons.append(lessonName)
    addedLessons += 1
    print(miniBrace)

print(brace)

# Dersler için not girme alanı
for lesson in lessons:
    print(f"Please write down the grade values for {lesson} courses.")
    
    midterm = pointControl(input("Please enter midterm note: "))
    final = pointControl(input("Please enter your final grade: "))
    project = pointControl(input("Please enter the project note: "))
    #print(midterm, final, project)
    lesson = Lesson(lesson, midterm, final, project)
    lesson.gradeCalculate()
    lesson.printResult()
    print(miniBrace)

print(brace)
print(miniBrace)
print("You gave a good education. Thank you. :)")
print(miniBrace)
print(brace)