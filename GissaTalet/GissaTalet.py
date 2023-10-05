from colors import bcolors
import random 
number_of_attempts = 7
user_attempts = 0
user_answer = 0
correct_answer = random.randint(1, 100)
print("Hello, let's try guessing a number 1-100")
print("You have 7 attempts")
while True:
    try:
        user_answer = int(input("Guess the number! "))
        if 1 == number_of_attempts: 
            print("You have no more attempts")
            break
        else:
            if user_answer == correct_answer:
                user_attempts =+ 1 
                print("Congratulations, the number was", correct_answer, "you won! And you needed", user_attempts,"attempts!")
                break
            elif user_answer > correct_answer:
                number_of_attempts = number_of_attempts -1
                user_attempts =+ 1 
                print("Too high! You have",number_of_attempts," attempts left!")
            else: 
                number_of_attempts = number_of_attempts -1
                user_attempts += 1
                print("Too low! You have",number_of_attempts, "attempts left!")
            
    except ValueError: 
        print("Type in only numbers! You didn't lose your attempt this time!")     