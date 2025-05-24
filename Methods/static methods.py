# Static methods = A method that belong to a class rather than any object from that class (Instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position ):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = {"Manager", "Cashier", "Cook", "Janitor"}
        return position in valid_position

employee1 = Employee("Engune", "Manager")
employee2 = Employee("miracle", "PMC adviser")
employee3 = Employee("nate", "lead engineer")

print(Employee.is_valid_position("rocket scientist"))
print(employee2.get_info())
print(employee1.get_info())
print(employee3.get_info())


