import os

file_path = "test"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("that is a directory")
else:
    print("That location doesn't exist")