


print()
print("Object Oriented Programming And Structure Learning")
print()

# class
class Student:
    university_name = "OSGU"

    def __init__(self,name,rollno,course):
        self.name = name
        self.rollno = rollno
        self.course = course

    def get_student_info(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
    
    @staticmethod
    def hello():
        print("Hello EveryOne")


# object
ajay = Student("ajay",211020151006,"BCA")
aman = Student("aman",211020151001,"BCA")

print(ajay)
print(ajay.university_name)
ajay.get_student_info()
ajay.hello()
aman.get_student_info()



# Inheritance

class Car:
    def __init__(self):
        print("car constructor called....")

    def __init__(self,name):
        print("car constructor called....{}".format(name))

    def start(self):
        print("start car.")
        print(self.name)

    def stop(self):
        print("stop car.")


class Tata(Car):
    def __init__(self,name):
        print("Tata Car contructor called.....")
        self.name = name
        super().__init__()
        super().__init__(self.name)
    

print("\n\n")
tc1 = Tata("maruti800")
tc1.start()
tc1.stop()