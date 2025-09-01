import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path     = os.path.join(working_directory, file_path)
    work_dir_abs  = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(full_path)

    if not file_path_abs.startswith(work_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 

    try:
        with open(file_path_abs, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Opens and writes to a file. It will also return the length of the content written.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write content to. Will provide an error if the file is outside of the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is to be written to the file.",
            ),
        },
    ),
)

    # os.path.abspath(): Get an absolute path from a relative path
    # os.path.join(): Join two paths together safely (handles slashes)
    # .startswith(): Check if a string starts with a substring
    # os.path.isdir(): Check if a path is a directory
    # os.listdir(): List the contents of a directory
    # os.path.getsize(): Get the size of a file
    # os.path.isfile(): Check if a path is a file
    # .join(): Join a list of strings together with a separator
