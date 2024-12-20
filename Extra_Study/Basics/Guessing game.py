import random
secret_number = random.randint(1, 50)
limit = 3



while limit != 0:
    my_guess = int(input("Guess a number between 1 and 50: "))
    if my_guess > secret_number:
        print("Your guess is too high")
        limit -= 1
        if limit == 0:
            break
        print(f"You have {limit} guesses left.")
    elif my_guess < secret_number:
        print("Your guess is too low")
        limit -= 1
        if limit == 0:
            break
        print(f"You have {limit} guesses left.")
    else:
        print("You win!")
        break
else:
    print("You lose!")

print("The secret number is", secret_number)
