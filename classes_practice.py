class student:
    #Class Attribute - shared by alll instances of student
    #this is the same for every student
    
    school = "Shiz University"
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_info(self):
        return f"{self.name} is {self.age} in grade {self.grade} at {self.school}. "
    
# Creating two instances of the student class
student1 = student("Alice", 20, "Sophomore")
student2 = student("Bob", 22, "Senior")

# Printing information for both students
print(student1.get_info())
print(student2.get_info())