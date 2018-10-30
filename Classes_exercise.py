class Student:
    """ This is a class for Students """

    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = [course]
        self.grade = [grade]

    def add_course_grade(self, course, grade):
        self.course.append(course)
        self.grade.append(grade)

    def __str__(self):
        output = "Name: " + str(self.name) + "\n"
        output += "Age: " + str(self.age) + "\n"
        for i in range(0, len(self.course)):
            output += "Course " + str(i+1) + ": " + str(self.course[i]) + " (" + str(self.grade[i]) + ")" + "\n"
        return output[:-1]

Test = Student('Dominik', 25, 'MADS', 1.0)
print(Test)

Test.add_course_grade("Blockchain", 2.3)
print(Test)
        
