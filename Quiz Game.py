
import random
easy_questions = {

    "What does CPU stand for?":
    "central processing unit",

    "What does RAM stand for?":
    "random access memory",

    "Which function is used to display output in Python?":
    "print",

    "Which function is used to take input from the user?":
    "input",

    "Which keyword is used for conditions?":
    "if",

    "Which symbol is used for comments in Python?":
    "#",

    "Which keyword is used to import a module?":
    "import",

    "Which keyword is used to define a function?":
    "def",

    "Which data type stores True or False values?":
    ["bool", "boolean"],

    "Which data type stores multiple values?":
    ["list", "lists"]
}

medium_questions = {

    "Which keyword is used for loops in Python?":
    ["while", "for"],

    "What does HTML stand for?":
    "hyper text markup language",

    "What does SQL stand for?":
    "structured query language",

    "What does OOP stand for?":
    "object oriented programming",

    "Which symbol is used for assignment in Python?":
    "=",

    "Which data structure follows FIFO?":
    ["queue"],

    "Which data structure follows LIFO?":
    ["stack"],

    "Which Python data type is immutable: list or tuple?":
    ["tuple"],

    "What is the full form of DBMS?":
    "database management system",

    "Which SQL clause is used to group rows?":
    ["group by"]
}

hard_questions = {

    "Which traversal of a BST gives sorted output?":
    ["inorder", "in-order"],

    "What is the worst case time complexity of Quick Sort?":
    ["o(n^2)", "n^2"],

    "What is the average case time complexity of Binary Search?":
    ["o(log n)", "log n"],

    "Which algorithm is used to find the shortest path in a graph?":
    ["dijkstra", "dijkstra's algorithm"],

    "Which algorithm is used to find Minimum Spanning Tree?":
    ["kruskal", "prim", "kruskal's algorithm", "prim's algorithm"],

    "Which graph algorithm uses indegree values?":
    ["topological sort"],

    "What is the space complexity of Merge Sort?":
    ["o(n)", "n"],

    "Which SQL join returns only matching records from both tables?":
    ["inner join"],

    "What does ACID stand for in DBMS?":
    ["atomicity consistency isolation durability"],

    "Which data structure is used in recursion?":
    ["stack"]
}

score = 0
questions_answered = 0
easy_asked = []
medium_asked = []
hard_asked = []

while True:
    print("\n----QUIZ GAME----")

    print("1. Easy Quiz")
    print("2. Medium Quiz")
    print("3. Hard Quiz")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        questions = easy_questions
        asked_questions = easy_asked

    elif choice == "2":
        questions = medium_questions
        asked_questions = medium_asked

    elif choice == "3":
        questions = hard_questions
        asked_questions = hard_asked


    elif choice == "4":

        print("Exiting Quiz Game...")
        break

    else:

        print("Invalid Choice")
        continue

    print("\nStarting Quiz....")

    available_questions = []

    for q in questions.keys():

        if q not in asked_questions:
            available_questions.append(q)


    question = random.choice(available_questions)

    asked_questions.append(question)

    print("\nQuestion:", question)

    answer = input("Enter your answer: ").lower()

    correct_answer = questions[question]

    if isinstance(correct_answer, list):

        if answer in correct_answer:

            print("Correct answer!")
            score += 1

        else:

            print("Wrong answer")

    else:

        if answer == correct_answer:

            print("Correct answer!")
            score += 1

        else:

            print("Wrong answer")

    questions_answered += 1

    print("\n------Score Board------")
    print("Questions answered:", questions_answered)
    print("Total Score:", score)

    accuracy = (score / questions_answered) * 100
    print("Accuracy:", round(accuracy, 2), "%")

    if len(asked_questions) == len(questions):
        print("\nYou have answered all questions!")

        print("\n------ FINAL SCORE BOARD ------")
        print("Questions Answered:", questions_answered)
        print("Total Score:", score)

        accuracy = (score / questions_answered) * 100
        print("Accuracy:", round(accuracy, 2), "%")

        print("\nYou completed this difficulty!")
        continue

import random
easy_questions = {

    "What does CPU stand for?":
    "central processing unit",

    "What does RAM stand for?":
    "random access memory",

    "Which function is used to display output in Python?":
    "print",

    "Which function is used to take input from the user?":
    "input",

    "Which keyword is used for conditions?":
    "if",

    "Which symbol is used for comments in Python?":
    "#",

    "Which keyword is used to import a module?":
    "import",

    "Which keyword is used to define a function?":
    "def",

    "Which data type stores True or False values?":
    ["bool", "boolean"],

    "Which data type stores multiple values?":
    ["list", "lists"]
}

medium_questions = {

    "Which keyword is used for loops in Python?":
    ["while", "for"],

    "What does HTML stand for?":
    "hyper text markup language",

    "What does SQL stand for?":
    "structured query language",

    "What does OOP stand for?":
    "object oriented programming",

    "Which symbol is used for assignment in Python?":
    "=",

    "Which data structure follows FIFO?":
    ["queue"],

    "Which data structure follows LIFO?":
    ["stack"],

    "Which Python data type is immutable: list or tuple?":
    ["tuple"],

    "What is the full form of DBMS?":
    "database management system",

    "Which SQL clause is used to group rows?":
    ["group by"]
}

hard_questions = {

    "Which traversal of a BST gives sorted output?":
    ["inorder", "in-order"],

    "What is the worst case time complexity of Quick Sort?":
    ["o(n^2)", "n^2"],

    "What is the average case time complexity of Binary Search?":
    ["o(log n)", "log n"],

    "Which algorithm is used to find the shortest path in a graph?":
    ["dijkstra", "dijkstra's algorithm"],

    "Which algorithm is used to find Minimum Spanning Tree?":
    ["kruskal", "prim", "kruskal's algorithm", "prim's algorithm"],

    "Which graph algorithm uses indegree values?":
    ["topological sort"],

    "What is the space complexity of Merge Sort?":
    ["o(n)", "n"],

    "Which SQL join returns only matching records from both tables?":
    ["inner join"],

    "What does ACID stand for in DBMS?":
    ["atomicity consistency isolation durability"],

    "Which data structure is used in recursion?":
    ["stack"]
}

score = 0
questions_answered = 0
easy_asked = []
medium_asked = []
hard_asked = []

while True:
    print("\n----QUIZ GAME----")

    print("1. Easy Quiz")
    print("2. Medium Quiz")
    print("3. Hard Quiz")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        questions = easy_questions
        asked_questions = easy_asked

    elif choice == "2":
        questions = medium_questions
        asked_questions = medium_asked

    elif choice == "3":
        questions = hard_questions
        asked_questions = hard_asked


    elif choice == "4":

        print("Exiting Quiz Game...")
        break

    else:

        print("Invalid Choice")
        continue

    print("\nStarting Quiz....")

    available_questions = []

    for q in questions.keys():

        if q not in asked_questions:
            available_questions.append(q)


    question = random.choice(available_questions)

    asked_questions.append(question)

    print("\nQuestion:", question)

    answer = input("Enter your answer: ").lower()

    correct_answer = questions[question]

    if isinstance(correct_answer, list):

        if answer in correct_answer:

            print("Correct answer!")
            score += 1

        else:

            print("Wrong answer")

    else:

        if answer == correct_answer:

            print("Correct answer!")
            score += 1

        else:

            print("Wrong answer")

    questions_answered += 1

    print("\n------Score Board------")
    print("Questions answered:", questions_answered)
    print("Total Score:", score)

    accuracy = (score / questions_answered) * 100
    print("Accuracy:", round(accuracy, 2), "%")

    if len(asked_questions) == len(questions):
        print("\nYou have answered all questions!")

        print("\n------ FINAL SCORE BOARD ------")
        print("Questions Answered:", questions_answered)
        print("Total Score:", score)

        accuracy = (score / questions_answered) * 100
        print("Accuracy:", round(accuracy, 2), "%")

        print("\nYou completed this difficulty!")
        continue
