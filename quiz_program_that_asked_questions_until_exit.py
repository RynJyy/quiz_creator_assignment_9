# Import necessary modules
import json
import random
from colorama import Fore, Style, init

# Initialize colorama for colored text
init (autoreset=True)

# Function to display a fancy header
def show_header():
    print(Fore.BLUE + "=" * 34)
    print(Fore.MAGENTA + "📚 Welcome to the quiz creator! 📚")
    print(Fore.BLUE + "=" * 34 + "\n")
    # Add a description on how to use the program
    print(Fore.CYAN + "This program allows you to create your own quiz questions.")
    print(Fore.CYAN + "You can add questions, specify answers, and save them for later use.\n")

# Function to get a quiz question from the user
def get_question():
    print(Fore.YELLOW + "\nEnter a new quiz question:")
    question = input(Fore.GREEN + "Question: ")
    # Collect four possible answers (a, b, c, d)
    answers = []
    for option in ['a', 'b', 'c', 'd']:
        answer = input(Fore.GREEN + f"Option {option}: ")
        answers.append(answer)
    # Get the correct answer from the user (validate input)
    while True:
        correct_answer = input(Fore.GREEN + "Correct answer (a/b/c/d): ").lower()
        if correct_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print(Fore.RED + "Invalid input. Please enter a, b, c, or d.")
    # Get question category
    category = input(Fore.GREEN + "Category: ")
    # Get difficulty level
    difficulty = input(Fore.GREEN + "Difficulty (intro/beginner/intermediate): ").lower()
    while difficulty not in ['intro', 'beginner', 'intermediate']:
        print(Fore.RED + "Invalid input. Please enter intro, beginner, or intermediate.")
        difficulty = input(Fore.GREEN + "Difficulty (intro/beginner/intermediate): ").lower()
    # Return the collected data as a dictionary
    return {
            'question': question,
            'answers': answers,
            'correct_answer': correct_answer,
            'category': category,
            'difficulty': difficulty
        }

# Function to save quiz data to a file
def save_quiz_data(data, filename='quiz_questions.json'):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    except json.JSONDecodeError:
        existing_data = []
    # Append new question data to the existing list
    existing_data.append(data)
    # Save updated data back to the file
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)
    print(Fore.GREEN + "Quiz question saved successfully!")

# Main function to control the quiz creator
def main():
    show_header()
    # Loop to keep asking for new questions until user exits
    while True:
        question_data = get_question()
        save_quiz_data(question_data)
        # Ask if the user wants to add another question
        another = input(Fore.YELLOW + "Do you want to add another question? (yes/no): ").lower()
        if another != 'yes':
            print(Fore.BLUE + "Thank you for using the quiz creator your file is now saved!")
            break
# Execute the main function when the script runs
if __name__ == "__main__":
    main()

