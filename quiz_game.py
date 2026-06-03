questions = (("Which keyword is used to create a function in python ? :"),
             ("Which of the folowing is an output device ? :"),
             ("Which data type stores multiple terms in a single variable ? :"),
             ("Wwhich python collection does not allow duplocate value ? :"),
             ("which of the folowing is mutuable ? :"))

options = (("A. function","B. define","C. def","D. func"),
           ("A. Keyword","B. Mouse","C. Monitor","D. Scanner"),
           ("A. int","B. float","C. list","D. bool"),
           ("A. List","B. Tuple","C. Set","D. Dictionary"),
           ("A. Tuple","B.String","C. List","D. Integer"))

answers = ("C","C","C","C","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+= 1
        print("CORRECT")
    else :
        print("INCORRECT")
        print(f"{answers[question_num]} is correct answer")
    question_num+= 1

print("--------------------------------")
print("              RESULT            ")
print("--------------------------------")

print("answers: ", end = " ")
for answer in answers:
    print(answer , end = " ")
print()

print("guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()    

score =int(score/len(questions)*100)
print(f"Your score is : {score}%" )