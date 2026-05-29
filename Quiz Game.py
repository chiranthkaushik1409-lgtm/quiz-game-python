
import random
questions = {
    "What does CPU stand for?": "central processing unit",

    "Which keyword is used for loops in Python?":
    ["while", "for"],

    "What does RAM stand for?":
    "random access memory",

    "Which keyword is used to define a function in Python?":
    "def",

    "Which data type stores multiple values?":
    ["list", "lists"],

    "Which symbol is used for comments in Python?":
    "#",

    "Which keyword is used for conditions?":
    "if",
"Which keyword is used to create a class in Python?":
"class",

"What does HTML stand for?":
"hyper text markup language",

"What does SQL stand for?":
"structured query language",

"Which function is used to display output in Python?":
"print",

"Which function is used to take input from the user?":
"input",

"Which data type stores True or False values?":
["bool", "boolean"],

"What symbol is used for assignment in Python?":
"=",

"Which keyword is used to import a module?":
"import",

"What does OOP stand for?":
"object oriented programming",

"Which keyword is used to define a loop that runs while a condition is true?":
"while"

}

score = 0
questions_answered = 0
asked_questions = []

while True:
    print("\n----QUIZ GAME----")

    print("1. Start Quiz")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice=='1':

        print("\n Starting Quiz....")

        available_questions =[]

        for q in questions.keys():
            if q not in asked_questions:
                available_questions.append(q)

        if len(asked_questions) == len(questions):
            print("\nYou have answered all questions!")

            print("\n------ FINAL SCORE BOARD ------")
            print("Questions Answered:", questions_answered)
            print("Total Score:", score)

            print("\nThank You for playing!!")
            break

        question= random.choice(available_questions)

        asked_questions.append(question)

        print("\n Question:", question)
        answer = input("Enter your answer:").lower()
        questions_answered+=1
        correct_answer = questions[question]

        if isinstance(correct_answer,list):
           if answer in correct_answer:
               print("Correct answer!")
               score+= 1

           else:
               print("Wrong answer")

        else:
             if answer == correct_answer:
                print("Correct answer!")
                score+= 1

             else:
                 print("Wrong answer")



        print("\n------Score Board-------")
        print("Questions answered:",questions_answered)
        print("Total Score:",score)
    elif choice =='2':
         print("Exiting Quiz Game...")
         break
    else:
        print('Invalid Choice')

