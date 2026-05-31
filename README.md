# Quiz Game 🧠

A command-line quiz game built in Python featuring three difficulty levels, randomized questions, duplicate prevention, score tracking, and accuracy statistics.

## Features

* Three difficulty levels — Easy, Medium, and Hard
* 30 questions across three difficulty levels
* Separate question banks for each difficulty
* Random question selection using Python's `random` module
* Duplicate prevention — questions do not repeat within a difficulty level
* Supports multiple valid answers where applicable
* Live scoreboard after every round
* Accuracy percentage tracking
* Final scoreboard displayed automatically after all questions in a difficulty level are answered
* Exit option available from the main menu

## Concepts Used

* Dictionaries to store questions and answers
* Lists to track answered questions
* `random.choice()` for random question selection
* `isinstance()` to handle single and multiple correct answers
* While loops for the game loop
* Conditional statements (`if`, `elif`, `else`)
* Variables for score and accuracy tracking
* Input normalization using `.lower()`
* Membership operator (`in`) for answer validation

## What I Learned

* Working with dictionaries and lists in Python
* Using randomization with `random.choice()`
* Tracking user progress using variables
* Handling multiple correct answers
* Preventing duplicate questions
* Calculating and displaying accuracy percentages
* Building a menu-driven Python application
* Writing cleaner and more organized code

## How to Run

1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python "Quiz Game.py"
```

## Future Improvements

* Timer-based quiz mode
* More question categories
* Difficulty-specific scoring
* Question loading from external files
* GUI version using Tkinter or PyQt
* Leaderboard system

## Author

**Chiranth R Kaushik**

GitHub: @chiranthkaushik1409-lgtm

