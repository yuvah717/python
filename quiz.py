print("===== PYTHON QUIZ =====")
print("10 Questions | 10 Marks")
print()

score = 0

questions = [
    ("1. What is the correct extension for a Python file?",
     ["A) .html", "B) .py", "C) .java", "D) .css"], "B"),

    ("2. Which keyword is used to create a function in Python?",
     ["A) function", "B) define", "C) def", "D) fun"], "C"),

    ("3. Which symbol is used for comments in Python?",
     ["A) //", "B) #", "C) /*", "D) --"], "B"),

    ("4. Which data type stores True or False?",
     ["A) String", "B) Integer", "C) Boolean", "D) Float"], "C"),

    ("5. Which function is used to display output?",
     ["A) input()", "B) print()", "C) output()", "D) display()"], "B"),

    ("6. Which operator is used for addition?",
     ["A) +", "B) -", "C) *", "D) /"], "A"),

    ("7. Which function is used to get input from the user?",
     ["A) get()", "B) input()", "C) scan()", "D) read()"], "B"),

    ("8. Which one is a Python list?",
     ["A) {1, 2, 3}", "B) (1, 2, 3)", "C) [1, 2, 3]", "D) <1, 2, 3>"], "C"),

    ("9. Which keyword is used for a condition?",
     ["A) if", "B) when", "C) check", "D) condition"], "A"),

    ("10. Which keyword is used to stop a loop?",
     ["A) stop", "B) exit", "C) break", "D) end"], "C")
]

for question, options, answer in questions:
    print(question)

    for option in options:
        print(option)

    user_answer = input("Your answer: ").upper()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    print()

print("===== QUIZ COMPLETED =====")
print("Your score:", score, "/ 10")
print("Percentage:", score * 10, "%")
