class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def getDetails(self):
        return f"Name: {self.name} Age: {self.age} Grade: {self.grade}"
    
    def getAge(self):
        return f"Age is: {self.age}"
    def getGrade(self):
        return f"Grade is: {self.grade}"
    def getName(self):
        return f"Name is: {self.name}"
    
Student1 = Student("Buze",24,12)
print(Student1.getAge())
print(Student1.getGrade())
print(Student1.getDetails())