from colors import bcolors
import random

number_of_attempts = 7
user_attempts = 0
user_answer = 0
correct_answer = random.randint(1, 100)

print("Hi! Let's try guessing a number from 1 to 100.")
print("You have only 7 attempts.")

running = True

while running:
    number_of_attempts = 7
    print(correct_answer)
       
    while True:
        try:
            user_answer = int(input("Guess the number! "))
        except ValueError:
            print("Only numbers! You haven't lose your attempt this time!")
            continue    
        if number_of_attempts == 1:
            print("You have no more attempts.")
            print("The number was",correct_answer)            
            break
        else:
            if user_answer == correct_answer:
                user_attempts = 1
                print("Congratulations, the number was", correct_answer, "you won! You only needed", user_attempts,"attempts!")
                break          
            elif user_answer > correct_answer:
                number_of_attempts -= 1
                user_attempts += 1
                print("Too low! You have",number_of_attempts,"attempts left!")
            else:
                number_of_attempts -= 1
                user_attempts += 1
                print("Too high! You have",number_of_attempts, "attempts left!")
               
    restart_game = input("Try again? Yes/No ").upper()  
    if restart_game == "YES":
        number_of_attempts = 7
    else:
        print("ending the game")
        break
