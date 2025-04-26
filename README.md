# 📚 Quiz Creator & Quiz App 🎉

Welcome to the **Quiz Creator and Quiz App** project!  
This project is divided into two parts:

- **Part 1:** A CLI (Command-Line Interface) Quiz Creator to create and save quiz questions.
- **Part 2:** A GUI (Graphical User Interface) Quiz App to play the quiz based on saved questions.

## 🛠️ Part 1: Quiz Creator (CLI)

This is a simple interactive Python program that allows users to create their own quiz questions. It collects multiple-choice questions, stores them in a JSON file, and ensures data validation for accuracy.

---

## Features 🚀
- Create custom quiz questions interactively
- Supports multiple-choice questions (a, b, c, d)
- Categorize questions and set difficulty levels
- Saves questions in a structured JSON format
- User-friendly interface with colored text (using `colorama`)

---

## Example Output 🎮
```
==================================
📚 Welcome to the quiz creator! 📚
==================================
This program allows you to create your own quiz questions.
You can add questions, specify answers, and save them for later use.

Enter a new quiz question:
Question: What is the capital of Philippines?
Option a: Berlin
Option b: Madrid
Option c: Manila
Option d: Rome
Correct answer (a/b/c/d): c
Category: Geography
Difficulty (intro/beginner/intermediate): beginner
Quiz question saved successfully!
Do you want to add another question? (yes/no): no
Thank you for using the quiz creator your file is now saved!
```

---

## 🎨 Part 2: Quiz App (GUI)

### Description:
The **Quiz App** loads the saved quiz questions and provides a colorful, interactive way for users to test their knowledge.

### Features:
- Randomized question selection.
- Colorful pastel buttons.
- Real-time feedback for correct or wrong answers.
- Final score display with percentage.
- Simple exit button.

### GUI Preview:
- Questions displayed in a fun font with a black background.
- Answer options in colorful pastel buttons.
- Real-time feedback like "Correct! 🎉" or "Wrong! 😢".
- Final score popup showing total score and percentage.

---

## ⚡ Notes:
- Make sure to create some quiz questions with the **Quiz Creator** first before running the **Quiz App**.
- The `quiz_questions.json` file must exist for the GUI app to work correctly.
- You can edit or add more questions directly in the JSON file if needed (advanced).
