import os

def get_files_info(working_directory, directory="."):
    full_path    = os.path.join(working_directory, directory)
    
    work_dir_abs = os.path.abspath(working_directory)
    dir_abs      = os.path.abspath(full_path)

    if not dir_abs.startswith(work_dir_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(dir_abs):
        return f'Error: "{directory}" is not a directory'

    dir_contents_list = os.listdir(dir_abs)
    
    if directory == ".":
        contents_string = "Results for current directory:\n"
    else:
        contents_string = f"Results for '{directory}' directory:\n" 
    for item in dir_contents_list:
        item_path = os.path.join(dir_abs, item)
        contents_string += f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isfile(item_path)}"
        if item != dir_contents_list[-1]:
            contents_string += "\n"

    return contents_string

def get_file_content(working_directory, file_path):
    work_dir_abs  = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(file_path)

    if not file_path_abs.startswith(work_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 

    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000

    try:
        with (file_path_abs, "r") as file:
            file_string = file.read(MAX_CHARS)

    except Exception as e:
        print(f"Error: {e}")


    # os.path.abspath(): Get an absolute path from a relative path
    # os.path.join(): Join two paths together safely (handles slashes)
    # .startswith(): Check if a string starts with a substring
    # os.path.isdir(): Check if a path is a directory
    # os.listdir(): List the contents of a directory
    # os.path.getsize(): Get the size of a file
    # os.path.isfile(): Check if a path is a file
    # .join(): Join a list of strings together with a separator
