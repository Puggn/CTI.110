#Elijah Gonzalez
#12/7/2023
#CTI-110 P5HW
#Functoins, random numbers, and while loop

import random

#Displays Menu
def show_menu():
    print("Welcome to math Quiz")
    print()
    print()
    print("MAIN MENU")
    print("------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()

#this function adds two random numbers

def add():
    rand_1 = random.randint(0, 10)
    rand_2 = random.randint(0, 10)
    print(f"{rand_1} + {rand_2}")
    return (rand_1 + rand_2)

#this function subtracts two random numbers
def subtract():
    rand_1 = random.randint(0, 10)
    rand_2 = random.randint(0, 10)
    print(f"{rand_1} - {rand_2}")
    return (rand_1 - rand_2)

#Ths function simulates the user guessing.
#While the guess is wrong, allow the user to guess again
def guessing(guess, answer):
    num_guesses = 0
    while guess != answer:
       num_guesses += 1
       if guess > answer: #If the user guessed too high
           print('Your guess is too high')
           guess = int(input('What is your guess: '))
       else:       #If user guesses too low
            print('your guess is too low')
            guess = int(input('What is your guess: '))
    #user answer is correct, the while loop breaks
    print('Your answer is correct!!!!')
    print(f"It took you {num_guesses} incorrect guesses to get it right... wow.")

    

#Main function
def main():
    show_menu()
    user_option = int(input("Please choose a menu option: "))
    while user_option != 3:
        if user_option == 1:
            rand_sum = add()   #represents the correct answer
            my_guess = int(input("What is your guess? ")) #represent guess
            guessing(my_guess, rand_sum)
            show_menu()
            user_option = int(input("Please choose a menu option: "))
        if user_option == 2:
            rand_sum = subtract()   #represents the correct answer
            my_guess = int(input("What is your guess? ")) #represent guess
            guessing(my_guess, rand_sum)
            show_menu()
            user_option = int(input("Please choose a menu option: "))
    #If user_choice ==3, the while loop breaks
    print("Thank you for playing, GoodBye :c")

#Call the main function
if __name__ == "__main__":
    main()
    


    

