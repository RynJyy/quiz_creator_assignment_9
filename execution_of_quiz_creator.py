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
        result_label.config(text="Correct!", fg="#90ee90")  # Light green
        score += 1
    else:
        result_label.config(text=f"Wrong! Correct: {correct}", fg="#ff7f7f")  # Soft red

    questions_asked += 1
    if questions_asked < total_questions:
        window.after(1000, next_question)
    else:
        window.after(1000, show_final_score)

# Display next question
def next_question():
    global current_question
    current_question = random.choice(quiz_data)

    question_label.config(text=current_question['question'])

    for i, option in enumerate(['a', 'b', 'c', 'd']):
        answer_buttons[i].config(
            text = current_question['answers'][i],
            command = lambda opt=option: check_answer(opt),
            bg = "white",
            activebackground = "#d9d9d9"  # Light gray on click
        )

    result_label.config (text="")

# Show final score
def show_final_score():
    percentage = (score / total_questions) * 100
    messagebox.showinfo("Quiz Finished", f"Your Score: {score}/{total_questions}\nPercentage: {percentage:.2f}%")
    window.destroy()

# Set up main window
window = tk.Tk()
window.title("✨ Quiz App ✨")
window.geometry("550x550")
window.configure(bg="white") 

quiz_data = load_quiz_data()
score = 0
questions_asked = 0
total_questions = len(quiz_data)

current_question = None

# Widgets
question_label = tk.Label(window, text="", wraplength=500, font=("Helvetica", 18, "bold"), bg="white", fg="black")
question_label.pack(pady=30)

answer_buttons = []
for i in range(4):
    btn = tk.Button(window, text="", width=30, height=2, font=("Helvetica", 12), fg="black", bg="white", relief="ridge")
    btn.pack(pady=8)
    answer_buttons.append(btn)

result_label = tk.Label(window, text="", font=("Helvetica", 16, "bold"), bg="white", fg="black")
result_label.pack(pady=15)

exit_button = tk.Button(window, text="Exit Quiz", command=window.destroy, bg="white", fg="black",
                        font=("Helvetica", 12, "bold"), width=15, height=2, relief="ridge")
exit_button.pack(pady=20)

# Start the first question
if quiz_data:
    next_question()
else:
    question_label.config(text="No quiz data available.")

window.mainloop()