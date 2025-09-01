import os
from google.genai import types

def get_file_content(working_directory, file_path):
    full_path     = os.path.join(working_directory, file_path)
    work_dir_abs  = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(full_path)

    if not file_path_abs.startswith(work_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000

    try:
        with open(file_path_abs, "r") as file:
            file_string = file.read(MAX_CHARS)
            return file_string

    except Exception as e:
        print(f"Error: {e}")

            # file.write(content)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves and returns the content of a file in the specified directory, constrained to the working directory. Has a hard-coded character limit of 10000.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to retrieve content from. Will provide an error if the file is outside of the working directory or is not found.",
            ),
        },
    ),
)
