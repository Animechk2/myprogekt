"""class Student:
    amount_of_students = 0
    def __init__(self, height = 160):
        self.height = height
        Student.height +=1
    def grow(self, height=1):
        self.height+=height

nick = Student()
kate = Student(height = 170)
nike.grow(height=15)
alice = Student(height = 160)
print(nick.height)
print(kate.height)
"""
"""class Student:

    def __init__(self):
        self.heighr = 150
    height = 170
    def printer(self):
        print(self.height)
        #self.height +=10
        
        
nike = Student()
nike.printer()
#kate = Student()
#kolya = Student()"""
class Student:
    def __init__(self, name = None):
        self.name = name
        #def  __str__(self):
          #  return f"am a student. My name is{self.name}"
    def __del__(self):
        print("Training is over. I am expert")
nick = Student(name="Nick")
print(nick)