# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#              1. try, 2.except, 3.finally
# E.g.
# try:
#     # try some code
# except "Exception":
#     # Handle an Exception
# finally:
#     # do some clean up

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT! ")
except ValueError:
    print(f"Enter only number please! ")
except Exception:
    print("something went wrong!")
finally:
    print("Do some cleanup on aisle 1")