# Object-Oriented Programming
# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.year} {self.model}")

    def stop(self):
        print(f"you stop the {self.color} {self.year} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("G-wagon", 2023, "gray", False)
car2 = Car("Escalade", 2021, "brown", True)
car3 = Car("Bugatti", 2024, "Blue", False)

car1.drive()
car3.stop()
car2.describe()
