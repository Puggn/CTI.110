#Elijah
#12/5/2023
#User-defined functions

#This function take a bool parameter an returns an ineger
def days_in_feb(is_leap):
    if is_leap == True:
        days = 29
    else:           #this represents uneven = False
        days = 28
    return days

#Create Main Function
def main():
    is_leap_year = False

    input_year = int(input("Enter a year: "))

      

    if (input_year % 4) == 0:      # inputYear is divisible by 4

      if (input_year % 100) == 0:   # inputYear is divisible by 100 (century year)

        if (input_year % 400) == 0: # inputYear is divisible by 400

          is_leap_year = True

        else:           # inputYear is not divisible by 400

          is_leap_year = False

      else:             # inputYear is not divisible by 100

        is_leap_year = True

    else:               # inputYear is not divisible by 4

      is_leap_year = False

    #Call our function
    num_days = days_in_feb(is_leap_year)
    print(f"The year {input_year} has {num_days} days in February")

#call main function:
if  __name__ == "__main__":
    main()
