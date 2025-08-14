from functions.run_python import *

print("First test")
print(run_python_file("calculator", "main.py")) # (should print the calculator's usage instructions)
print("=====================================")

print("Second test")
print(run_python_file("calculator", "main.py", ["3 + 5"])) # (should run the calculator... which gives a kinda nasty rendered result)
print("=====================================")

print("Third test")
print(run_python_file("calculator", "tests.py"))
print("=====================================")

print("Fourth test")
print(run_python_file("calculator", "../main.py")) # (this should return an error)
print("=====================================")

print("Fifth Test")
print(run_python_file("calculator", "nonexistent.py")) # (this should return an error)
print("=====================================")