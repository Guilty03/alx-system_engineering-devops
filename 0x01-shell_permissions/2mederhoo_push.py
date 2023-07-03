import subprocess
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to generate a commit message based on the file name
def generate_commit_message(file_name):
    # Process the file name with spaCy
    doc = nlp(file_name)

    # Extract nouns from the file name
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]

    # Construct the commit message
    if nouns:
        commit_message = f"Auto commit: Added {', '.join(nouns)}"
    else:
        commit_message = "Auto commit: Updated file"

    return commit_message

# Collect user input
file_name = input("Enter the file name: ")

# Open Emacs for text input
subprocess.run(['emacs', file_name])

# Generate the commit message
commit_message = generate_commit_message(file_name)

# Change file mode to u+x
subprocess.run(['chmod', 'u+x', file_name])

# Git commands
commands = [
    ['git', 'add', file_name],
    ['git', 'commit', '-m', commit_message],
    ['git', 'push']
]

# Execute Git commands
for command in commands:
    subprocess.run(command)

print("File created, changes committed, and pushed successfully!")
