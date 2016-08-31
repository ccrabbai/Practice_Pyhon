#Exercise 9
#Guessing game one
import random
print("This is a guessing game\nNumber is from 1 to 9")
print("To exit the game type 'stop'")
Random_Number = random.randint(1,9)
i = 0
while(True):
    user_guess = int(input("Guess the number: "))
    i += 1
    if Random_Number == user_guess:
        print("Correct!")
        stp = input("To exit the game type 'stop'\nTo continue enter 'go': ")
        if stp == 'stop'.lower() or str(user_guess) == 'stop'.lower():
            print("You guessed", i, "time(s)\nGOODBYE")
            break
        elif stp == 'go'.lower() or str(user_guess) == 'go'.lower():
            pass
    elif user_guess < Random_Number:
        print("Hmmm, ", user_guess, " is a bit lower")
    elif user_guess > Random_Number:
        print("Oh!,", user_guess, " is a bit higher!")
    else:
        print(user_guess, "is not a number")
