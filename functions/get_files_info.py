import os

def get_files_info(working_directory, directory="."):
    if directory != None:
        full_path = os.path.join(working_directory, directory)
    else:
        full_path = working_directory
    
    
    work_dir_abs = os.path.abspath(directory)

    if not work_dir_abs.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    dir_contents_list = os.listdir(full_path)
    contents_string   = ""
    for item in dir_contents_list:
        item_path = os.path.join(directory, item)
        contents_string += f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isfile(item_path)}"
        if item != dir_contents_list[-1]:
            contents_string += "\n"

    return contents_string


    # os.path.abspath(): Get an absolute path from a relative path
    # os.path.join(): Join two paths together safely (handles slashes)
    # .startswith(): Check if a string starts with a substring
    # os.path.isdir(): Check if a path is a directory
    # os.listdir(): List the contents of a directory
    # os.path.getsize(): Get the size of a file
    # os.path.isfile(): Check if a path is a file
    # .join(): Join a list of strings together with a separator
