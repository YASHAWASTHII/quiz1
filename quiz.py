print("Register now!")
register = input("Enter username: ")
password = input("Enter password: ")

print("\nLogin!")
user = input("Enter username: ")

if user != register:
    print("Username not found! Exiting...")
else:
    c = 0
    while c < 5:
        p = input("Enter password: ")
        if p == password:
            print("You have successfully logged in!")
            break
        else:
            print("You have entered the wrong password. Please try again!")
            c += 1
    else:
        print("Too many failed attempts! Exiting...")
        exit()

print("\nAttempt all 15 questions carefully!")

questions = (
    "What is '10' + '20'?: ",
    "What is the full form of REPL?: ",
    "What is 10 / 2?: ",
    "What is the result of 32 >> 2?: ",
    "What is the value of c after solving the expression - x = 10 / 2 * (3 >> 1) - 45 % 5?: ",
    "Who created the first DBMS?: ",
    "In which of the following formats is data stored in the database management system?: ",
    "Which of the following is not an example of DBMS?: ",
    "Which of the following is a feature of the database?: ",
    "Which of the following is a function of the DBMS?: ",
    "Which of the following sorting algorithms can be used to sort a random linked list with minimum time complexity?: ",
    "Which one of the following is an application of Stack Data Structure?: ",
    "Stack A has the entries a, b, c (with a on top). Stack B is empty. An entry popped out of Stack A can be printed immediately or pushed to Stack B. An entry popped out of Stack B can only be printed. In this arrangement, which of the following permutations of a, b, c are not possible?: ",
    "The five items: A, B, C, D, and E are pushed in a stack, one after another starting from A. The stack is popped four items and each element is inserted in a queue. Two elements are deleted from the queue and pushed back on the stack. Now, one item is popped from the stack. The popped item is?: ",
    "The minimum number of stacks needed to implement a queue is?: "
)

options = (
    ("A. 30", "B. '1020'", "C. 1020", "D. Addition is not possible"),
    ("A. Read-Evaluate-Print-Loop", "B. Read Entire Programming Logic", "C. Render Engine Program Language", "D. None"),
    ("A. 5", "B. 5.0", "C. 0", "D. None"),
    ("A. 32", "B. 8", "C. 16", "D. None"),
    ("A. 5", "B. 10", "C. 5.0", "D. 7.5"),
    ("A. Edgar Frank Codd", "B. Charles Bachman", "C. Charles Babbage", "D. None"),
    ("A. Text", "B. Image", "C. Table", "D. Graph"),
    ("A. MySQL", "B. Microsoft Access", "C. IBM DB2", "D. Google"),
    ("A. No-backup for the data stored", "B. User interface provided", "C. Lack of authentication", "D. Store data in multiple locations"),
    ("A. Storing data", "B. Multiple user access control", "C. Data integrity", "D. All of the above"),
    ("A. Insertion sort", "B. Quick sort", "C. Heap sort", "D. Merge sort"),
    ("A. Manage function calls", "B. Stock span problems", "C. Arithmetic equation evaluation", "D. All of the above"),
    ("A. BAC", "B. BCA", "C. CAB", "D. ABC"),
    ("A. A", "B. B", "C. C", "D. D"),
    ("A. 3", "B. 1", "C. 2", "D. 4")
)

answers = ("B", "A", "B", "B", "C", "B", "C", "D", "B", "D", "D", "D", "C", "D", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("\n----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("\n----------------------")
print("       RESULTS        ")
print("----------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int((score / len(questions)) * 100)
print(f"\nYour score is: {score_percentage}%")
