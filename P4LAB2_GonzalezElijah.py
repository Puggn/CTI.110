#Elijah Gonzalez
#11/28/2023
#Output range with increments of 5

#User inputs variables
int_1 = int(input("Enter an integer: "))
int_2 = int(input("Enter an larger integer: "))

#Program is using if statements to decied what to produce next
if int_1 < int_2:
    for num in range(int_1, int_2 + 1, 5):
        print(num)
else:
    print("You didn't enter it corrrectly... ")
    
    #While this input is invalid
    while int_1 > int_2 or int_1 == int_2:
        
        #User inputs variables
        int_1 = int(input("Enter an integer: "))
        int_2 = int(input("Enter an larger integer: "))
        
        #Program is using if statements to decied what to produce next
    for num in range(int_1, int_2 + 1, 5):
        print(num)    
        
