# @property = Decorator used to define a method as a property (it can accessed like an attribute )
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you (getter: to read, setter: to write, and deleter: to delete) method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")



rectangle = Rectangle(3, 4)

rectangle.width = 6
rectangle.height = 67

del rectangle.height
del rectangle.width
