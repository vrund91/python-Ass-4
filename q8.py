'''Write a Python class named Student with two instances student1, student2 and assign 
values to the instances' attributes. Print all the attributes of the student1, student2 
instances with their values in the given format'''

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def displayStudent(self):
        print("name:",self.name,",age:",self.age,",Grade:",self.grade)

student1=Student("ABC",19,"A+")
student2=Student("XYZ",20,"B")

student1.displayStudent()
student2.displayStudent()

