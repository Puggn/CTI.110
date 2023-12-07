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
    u_input = int(input("Please choose one of the menu options: "))

#this function adds two random numbers

def add():
    ran1 = random.randint(0, 10)
    ran2 = random.randint(0, 10)
    print(f"{ran1} + {ran2}")
    return (ran1 + ran2)

#this function subtracts two random numbers
def subtract():
    ran1 = random.randint(0, 10)
    ran2 = random.randint(0, 10)
    print(f"{ran1} - {ran2}")
    return (ran1 - ran2)

#Ths function simulates the user guessing.
#While the guess is wrong, allow the user to guess again
def guessing(guess, answer):
    num_guesses = 0
    while guess != answer:
       num_guesses += 1
       if guess > answer: #If the user guessed too high
           print('Your guess is too high')
       else:       #If user guesses too low
            print('your guess is too low')
    #user answer is correct, the while loop breaks
    print('Your answer is correct!!!!')
    print(f"It took you {num_guesses} incorrect guesses to get it right... wow.")

    

#Main function
def main():
    show_menu()
    user_option = int(input("Please choose a menu option: "))
    if user_option == 1:
        ran_sum = add()   #represents the correct answer
        my_guess = int(input("What is your guess? ")) #reoresent guess
        guessing(my_guess, ran_sum)

#Call the main function
if __name__ == "__main__":
    main()
    

