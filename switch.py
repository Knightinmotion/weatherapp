# Match-case statement (switch): An alternative to using many "elif" statements
#                                Execute some code if value matches a "case"
#                                Benefits: cleaner and syntax is more readable
# "|" this is an "or" operator

def main():
    week = int(input("Enter day of the week: "))

    def day_of_week(day):
        if day == 1:
            return "It is Sunday"
        elif day == 2:
            return "it is Monday"
        elif day == 3:
            return "it is Tuesday"
        elif day == 4:
            return "it's Wednesday"
        elif day == 5:
            return "it's Thursday"
        elif day == 6:
            return "it's friday"
        elif day == 7:
            return "it's saturday"
        else:
            return "Not a valid day"

    print(day_of_week(week))


if __name__ == "__main__":
    main()


def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return "this is a weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "this is a weekday"
        case _:
            return "nothing dey here"


print(is_weekend('Tuesday'))

# module = a file containing code you want to include in your program... to that, use an import statement
# all the available list of module in python print(help("modules"))

# variable scope = where a variable is and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# def func1():
#     x = 3
#     print(x)
# def func2():
#     x = 5
#     print(x)
# func1()
# func2()

# if __name__ == __main__: (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#               helps readability,
#               leaves no global variables,
#               avoid unintended execution)

# E.g. library = import library for functionality
#      when running library directly a help page
