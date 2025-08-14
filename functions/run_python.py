import subprocess
import os

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