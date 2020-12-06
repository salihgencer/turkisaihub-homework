class Lesson:
    
    midtermPertentage = 0.3
    finalPercentage = 0.5
    projectPercentage = 0.2

    def __init__(self, lessonName, midterm, final, project):
        self.lesson = lessonName
        self.midterm = round(float(midterm) * self.midtermPertentage)
        self.final = round(float(final) * self.finalPercentage)
        self.project = round(float(project) * self.projectPercentage)
    
    def gradeCalculate(self):
        sonuc = self.midterm + self.final + self.project

        if sonuc >= 90:
            self.lessonResult = "AA"
        elif sonuc >= 70 and sonuc <90:
            self.lessonResult = "BB"
        elif sonuc >= 50 and sonuc <70:
            self.lessonResult = "CC"
        elif sonuc >= 30 and sonuc <50:
            self.lessonResult = "DD"
        elif sonuc < 30:
            self.lessonResult = "FF"

    def printResult(self):
        print(f"You have graded {self.lessonResult} from this lesson.")