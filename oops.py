


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
    
    def __init__(self,name):
        print("car constructor called....{}".format(name))
    def __init__(self):
        print("car constructor called....")


    def start(self):
        print("start car.")
        print(self.name)

    def stop(self):
        print("stop car.")


class Tata(Car):
    def __init__(self,name):
        print("Tata Car contructor called.....")
        self.name = name
        
    

print("\n\n")
tc1 = Tata("maruti800")
tc1.start()
tc1.stop()



from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclasses must implement this method

    @abstractmethod
    def perimeter(self):
        pass

# Concrete subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)  # Implementation of abstract method
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Abstract classes cannot be instantiated directly
# shape = Shape()  # This would raise an error

# Subclass instances are allowed
circle = Circle(5)
print("Area:", circle.area())  # Output: Area: 78.5
print("Perimeter:", circle.perimeter())  # Output: Perimeter: 31.4


s = Shape()