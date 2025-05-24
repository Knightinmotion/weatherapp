# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating ")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    @staticmethod
    def speak():
        print("WOOF")

class Cat(Animal):
    @staticmethod
    def speak():
        print("meow")

class Mouse(Animal):
    @staticmethod
    def speak():
        print("squeak")

dog = Dog("Scooby")
cat = Cat("amy")
mouse = Mouse("riley")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
dog.speak()

# multiple Inheritance = Inherit from more than one parent class
#                         C(A, B)

# multilevel inheritance = Inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

#
# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating ")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping ")
#
# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit("Bugs")
# hawk = Hawk("stark")
# fish = Fish("lily")




# super() = function used in a child class to call methods from a parent class(superclass).
#           Allows you to extend the functionality of the inherited methods

from math import pi
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled "}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {pi * self.radius * self.radius }")
        super().describe()



class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {pi * self.width * self.height / 2}")
        super().describe()

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=8)
triangle = Triangle(color="green", is_filled=True, height=9, width=6)

square.describe()







