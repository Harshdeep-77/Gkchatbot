import requests
import random

# Function to fetch 10 general knowledge questions from Open Trivia DB
def fetch_gk_questions(amount=10):
    url = f"https://opentdb.com/api.php?amount={amount}&category=9&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']

# Simple chatbot loop to ask 5 random questions in English
def chatbot():
    questions = fetch_gk_questions()
    asked_questions = random.sample(questions, 5)
    
    print("Hello! I am your English GK chatbot. Let's start.\n")
    
    score = 0
    for i, q in enumerate(asked_questions, 1):
        print(f"Question {i}: {q['question']}")
        options = [q['correct_answer']] + q['incorrect_answers']
        random.shuffle(options)
        
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        answer = input("Your answer (enter the number): ")
        try:
            if options[int(answer) - 1] == q['correct_answer']:
                print("Correct answer!\n")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is: {q['correct_answer']}\n")
        except:
            print(f"Invalid input. The correct answer is: {q['correct_answer']}\n")
    
    print(f"Your score: {score} / 5")
    print("Thank you!")

if __name__ == "__main__":
    chatbot()
