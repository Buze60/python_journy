print('                                             WELCOME TO STUDENT MANAGEMENT SYSTEM!: ')

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
        
    def GetStudentInfo(self):
        return f'Student name:\n {self.name} \n Student age:\n {self.age} \n Student garade:\n {self.grade}'
        
student1 = Student('Bizuayehu',24,'C')
student2 = Student('John',22,'A')

choice = int(input('1 for grade A\n2 for grade B\n3 for Whole student info C\n4 Exist'))
while choice != 4:
    if choice == 1:
        get_Student = input('Enter Student Name: ')
        print(getattr(student2,get_Student,'the attribute not found!'))
    elif choice == 2:
        get_Student = input('Enter Student Name: ')
        print(getattr(student2,get_Student,'the attribute not found!'))
    elif choice == 3:
        print(Student.GetStudentInfo())
        
    else:
        print('Invalid choice, please try again. 😊')