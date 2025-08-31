import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) > 1:
    prompt = sys.argv[1]
else:
    print("ERROR: No prompt provided")
    sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

print(response.text)

if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


# You’re certainly on the right track! By checking len(sys.argv) > 1, you’re making sure the user provides at least one argument (the prompt). Nicely reasoned.

# Let’s ponder a few questions to deepen your understanding:

#     What would happen if a user wants to pass a prompt that contains spaces, like:

#     python3 main.py Why is Gandalf so wise?

#     What does sys.argv look like in that case?
#     How might you handle prompts with many words while still supporting single-word prompts?

# If you’d like a clue, think about how you might use slicing (sys.argv[1:]) and a string method to assemble all the words into a single prompt string!
