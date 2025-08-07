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

            file.write(content)

