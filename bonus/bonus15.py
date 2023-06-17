import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for i, alternative in enumerate(question["alternatives"]):
        print(i + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0

for i, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    print(f"Q{i + 1}: {result} - Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}")

print(score, "/", len(data))