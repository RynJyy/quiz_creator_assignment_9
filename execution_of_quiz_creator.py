# Import necessary modules
import random
import json
import tkinter as tk
from tkinter import messagebox
# Load quiz data from the JSON file
def load_quiz_data(filename='quiz_questions.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No questions found.")
        return []
# Check if user's answer is correct
# Display next question
# Show final score
# Set up main window
# Widgets
# Start the first question
