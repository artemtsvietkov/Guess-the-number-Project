from colors import bcolors
import random 
number_of_attempts = 7
user_attempts = 0
user_answer = 0
correct_answer = random.randint(1, 100)
print("Hello, let's try guessing a number 1-100")
print("You have 7 attempts")
running = True
    
while running:
    while True:
        try:
            user_answer = int(input("Guess the number! "))
        except ValueError: 
            print("Type in only numbers! You didn't lose your attempt this time!")     
        if 1 == number_of_attempts: 
            print("You have no more attempts")
            print("The number was",correct_answer)
            restart_game = input("Do you want to try again? Yes/No ")                
            if restart_game == "Yes,yes,YEs":
                running
            elif restart_game == "No,no,nO":
                running = False
            else:
                break
        else:
            if user_answer == correct_answer:
                user_attempts =+ 1 
                break
                
            elif user_answer > correct_answer:
                number_of_attempts = number_of_attempts -1
                user_attempts = user_attempts + 1
                print("Too high! You have",number_of_attempts," attempts left!")
            else: 
                number_of_attempts = number_of_attempts -1
                user_attempts = user_attempts + 1
                print("Too low! You have",number_of_attempts, "attempts left!")
            
    print("Congratulations, the number was", correct_answer, "you won! And you needed", user_attempts,"attempts!")
    restart_game = input("Do you want to try again? Yes/No").upper()                
    if restart_game == "YES":
        continue
    elif restart_game == "NO":
        running = False
    else:
        running = False