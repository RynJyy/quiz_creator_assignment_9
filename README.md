# Quiz Creator

📚 **Welcome to the Quiz Creator!** 📚

This is a simple interactive Python program that allows users to create their own quiz questions. It collects multiple-choice questions, stores them in a JSON file, and ensures data validation for accuracy.

---

## Features 🚀
- Create custom quiz questions interactively
- Supports multiple-choice questions (a, b, c, d)
- Categorize questions and set difficulty levels
- Saves questions in a structured JSON format
- User-friendly interface with colored text (using `colorama`)

---

## Installation 🔧
### Prerequisites
Make sure you have Python installed (Python 3 recommended).

### Install Dependencies
Run the following command to install required dependencies:
```bash
pip install colorama
```

---

## Usage 📝
1. Clone the repository:
```bash
git clone https://github.com/yourusername/quiz-creator.git
cd quiz-creator
```
2. Run the script:
```bash
python quiz_creator.py
```
3. Follow the prompts to enter quiz questions, answer choices, correct answers, categories, and difficulty levels.
4. Your questions will be saved in `quiz_questions.json`.

---

## File Structure 📂
```
quiz_creator/
│── quiz_creator.py   # Main script
│── quiz_questions.json  # Stored quiz questions (auto-generated)
│── README.md  # Project documentation
```

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
