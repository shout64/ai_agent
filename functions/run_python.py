import subprocess
import os
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path     = os.path.join(working_directory, file_path)
    work_dir_abs  = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(full_path)

    if not file_path_abs.startswith(work_dir_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found.'

    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.' 

    commands = ['python', file_path_abs]
    if args:
        commands.extend(args)

    try:
        result = subprocess.run(commands, capture_output=True, timeout=30, text=True, cwd=work_dir_abs)
        
        output = []
        if result.stdout:
            output.append(f"STDOUT: \n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR: \n{result.stderr}")
        if result.returncode != 0:
            output.append(f"\nProccess exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a given python file. Will check to make sure the file is in the permitted working directory and is a valid file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the python file to run. Will provide an error if the file is outside of the working directory or is not found.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The arguments to pass while running the given python file, if they exist.",
            ),
        },
    ),
)