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
def next_question():
    global current_question
    current_question = random.choice(quiz_data)

    question_label.config(text=current_question['question'])

    pastel_colors = ["#ffb6b9", "#c1c8e4", "#d5f4e6", "#fce1e4"]
    for i, option in enumerate(['a', 'b', 'c', 'd']):
        answer_buttons[i].config(
            text = current_question['answers'][i],
            command = lambda opt = option: check_answer(opt),
            bg = pastel_colors [i % len(pastel_colors)],
            activebackground = "#555555"  # Darker on click
        )

    result_label.config (text="")

# Show final score
def show_final_score():
    percentage = (score / total_questions) * 100
    messagebox.showinfo("Quiz Finished 🎀", f"Your Score: {score}/{total_questions}\nPercentage: {percentage:.2f}%")
    window.destroy()

# Set up main window
window = tk.Tk()
window.title("✨ Quiz App ✨")
window.geometry("550x550")
window.configure(bg="#000000")  # Black background

quiz_data = load_quiz_data()
score = 0
questions_asked = 0
total_questions = len(quiz_data)

current_question = None

# Widgets
question_label = tk.Label(window, text="", wraplength=500, font=("Comic Sans MS", 18, "bold"), bg="#000000", fg="white")
question_label.pack(pady=30)

answer_buttons = []
for i in range(4):
    btn = tk.Button(window, text="", width=30, height=2, font=("Comic Sans MS", 12), fg="#333333", relief="flat")
    btn.pack(pady=8)
    answer_buttons.append(btn)

result_label = tk.Label(window, text="", font=("Comic Sans MS", 16, "bold"), bg="#000000", fg="white")
result_label.pack(pady=15)

exit_button = tk.Button(window, text="Exit Quiz", command=window.destroy, bg="#000000", fg="black",
                        font=("Comic Sans MS", 12, "bold"), width=15, height=2, relief="ridge")
exit_button.pack(pady=20)

# Start the first question
if quiz_data:
    next_question()
else:
    question_label.config(text="No quiz data available.")

window.mainloop()