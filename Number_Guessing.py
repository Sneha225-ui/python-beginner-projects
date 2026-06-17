import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True 

print("PYTHON NUMBER GUESSING GAME")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = int(input("Enter your guess: "))
    if guess.is_digit():
        guess = int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print("That num is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("To low! Try again!")
        elif guess>answer :
            print("To high! Try again!")
        else:
            print("Correct! The answer was {answer}")
            print(f"Number of guessing: {guesses}")
