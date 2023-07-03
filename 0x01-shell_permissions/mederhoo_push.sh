#!/bin/bash

# Collect user input
read -p "Enter the file name: " file_name
echo "Enter the text to be written inside the file (Ctrl+X Ctrl+S to save and Ctrl+X Ctrl+C to exit Emacs): "
emacs -nw "$file_name"

read -p "Enter the Git commit message: " commit_message

# Change file mode to u+x
chmod u+x "$file_name"

# Git commands
commands=(
  "git add $file_name"
  "git commit -m '$commit_message'"
  "git push"
)

# Execute Git commands
for command in "${commands[@]}"; do
  eval "$command"
done

echo "File created, changes committed, and pushed successfully!"
