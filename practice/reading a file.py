#  python reading (.txt, .json, .csv)

file_path = "C:/Users/MIRACLE/OneDrive/Desktop/project.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file ")
