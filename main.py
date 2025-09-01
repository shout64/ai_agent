import os
import sys
from dotenv                     import load_dotenv
from google                     import genai
from google.genai               import types
from functions.get_files_info   import *
from functions.get_file_content import *
from functions.write_file       import *
from functions.run_python       import *

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Get prompt
if len(sys.argv) > 1:
    prompt = sys.argv[1]
else:
    print("ERROR: No prompt provided")
    sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

# List of available functions for LLM to call
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python,
    ]
)

# Get response
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt),
)

# Print response
if len(response.function_calls) > 0:
    for function in response.function_calls:
        print(f"Calling function: {function.name}({function.args})")    
else:
    print(response.text)

if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
