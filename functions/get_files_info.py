import os
from google.genai import types

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
        # file.write(content)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

