# Import necessary modules
import random
import json
import tkinter as tk
from tkinter import messagebox
# Load quiz data from the json file
def load_quiz_data(filename='quiz_questions.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No questions found.")
        return []
    
# Check if user's answer is correct
def check_answer(user_answer):
    global score, questions_asked, total_questions
    correct = current_question['correct_answer']
    if user_answer == correct:
        result_label.config(text="Correct! 🎉", fg="#90ee90")  # Light green
        score += 1
    else:
        result_label.config(text=f"Wrong! 😢 Correct: {correct}", fg="#ff7f7f")  # Soft red

    questions_asked += 1
    if questions_asked < total_questions:
        window.after(1000, next_question)
    else:
        window.after(1000, show_final_score)
        
# Display next question
# Show final score
# Set up main window
# Widgets
# Start the first question
