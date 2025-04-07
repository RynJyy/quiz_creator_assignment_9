# Import necessary modules
import json
import random
from colorama import Fore, Style, init
# Initialize colorama for colored text
init (autoreset=True)
# Function to display a fancy header
print (Fore.BLUE + "=" * 34)
print (Fore.MAGENTA + "📚 Welcome to the quiz creator! 📚")
print (Fore.BLUE + "=" * 34 + "\n")
# Add a description on how to use the program
print (Fore.CYAN + "This program allows you to create your own quiz questions.")
print (Fore.CYAN + "You can add questions, specify answers, and save them for later use.\n")
# Function to get a quiz question from the user
# Collect four possible answers (a, b, c, d)
# Get the correct answer from the user (validate input)
# Get question category
# Get difficulty level
# Return the collected data as a dictionary
# Function to save quiz data to a file
# Append new question data to the existing list
# Save updated data back to the file
# Main function to control the quiz creator
# Loop to keep asking for new questions until user exits
# Ask if the user wants to add another question
# Execute the main function when the script runs
