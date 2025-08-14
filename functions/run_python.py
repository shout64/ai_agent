def run_python_file(working_directory, file_path, args=[]):
    full_path     = os.path.join(working_directory, file_path)
    work_dir_abs  = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(full_path)

    if not file_path_abs.startswith(work_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    if not full_path.endswith('.py'):
        f'Error: "{file_path}" is not a Python file.' 

    
