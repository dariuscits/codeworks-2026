#Quiz made by Darius McCoy.

score = 0

questions = [
    {
        "question": "1.What's the capital of France?",
        "options": ["A. Berlin", "B. Wales", "C. Paris","D. Rome"],
        "answer" : "C"
    },

    {
        "question": "2.What's the capital of Brazil?",
        "options": ["A. Rio de Janeiro", "B. Amazon", "C. Sao Paulo","D. Brasila"],
        "answer" : "D"

    },

    {
        "question": "3.What's the capital of Finland?",
        "options": ["A. Annapolis", "B. Helsinki", "C. Seoul","D. Bridgetown"],
        "answer" : "B"

    },

    {
        "question": "4.What's the capital of Denmark?",
        "options": ["A. Bangkok", "B. Copenhagen", "C. Seoul","D. Queensland"],
        "answer" : "B"
    }

]

print("====Welcome to My Quiz====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Enter Your Anwser (A,B,C or D): ").strip().upper()

    if response == q["answer"]:
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect..The correct answer was {q['answer']}.\n")

print("=" * 40)
print(f"Your final score is {score}/{len(questions)}")

