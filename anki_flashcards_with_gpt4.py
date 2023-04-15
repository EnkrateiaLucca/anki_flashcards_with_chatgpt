import os
import openai
import clipboard

# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Get content from clipboard
clipboard_content = clipboard.paste()

# Create a conversation with ChatGPT
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"Create anki flashcards with the following text using a format like question;answer next line question;answer etc...{clipboard_content}."}
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.7,
    max_tokens=2000
)

generated_flashcards = response["choices"][0]["message"]["content"]

# Save flashcards to a file
with open("flashcards.txt", "w") as f:
    f.write(generated_flashcards)

print("Flashcards saved to 'flashcards.txt'")
