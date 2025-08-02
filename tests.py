from functions.get_files_info import *

print("Lorem test")
print(get_file_content("calculator", "lorem.txt"))

print("\nMain test")
print(get_file_content("calculator", "main.py"))

print("\nCalculator.py test")
print(get_file_content("calculator", "pkg/calculator.py"))

print("\nbin/cat test")
print(get_file_content("calculator", "/bin/cat"))

print("\nnot exist test")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
