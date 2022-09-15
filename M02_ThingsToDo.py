from operator import truediv

tryAgain = "y"
secret = int(input("Please enter a number between 1 ~ 10"))

while tryAgain == "y":
    guess = int(input("Please enter another number between 1~10"))
    if guess == secret:
     print("You guessed correctly!")
     tryAgain == "n"
    elif guess >= secret:
        print("Your guess was to high!")
        tryAgain = input("Would you like to try again? y or n")
    elif guess <= secret:
        print("Your number is to low!")
        tryAgain = input("Would you like to try again? y or n")


small = True
green = True

userAnswerOne = input("Is your item small? y or n")
userAnswerTwo = input("Is your item green? y or n")
if userAnswerOne == "y":
    if userAnswerTwo == "y":
        print("Your item is a pea.")
    elif userAnswerTwo == "n":
        print("Your item is a cherry.")
elif userAnswerOne == "n":
    if userAnswerTwo == "y":
        print("Your item is a watermelon.")
    elif userAnswerTwo == "n":
        print("Your item is a pumpkin.")

guess_me = 7
number = 1
counter = 0

while number <= guess_me:
    print("Number is too low")
    number = number + 1
    counter = counter + 1
    if number >= guess_me:
        print("oops")
        number = number - 1
        counter = counter + 1
else:
    print("The number was:", guess_me)
    print("It took,", counter, "attempts.")

guess_meTwo = 5
for number in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
    if number <= guess_meTwo:
        print("Too low")
    elif number == guess_meTwo:
        print("Found it!")
        quit()
    elif number >= guess_meTwo:
        print("oops")
        quit()

quit()
