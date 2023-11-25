#CTI-110
#P3HW2 - Salary
#Elijah Gonzalez
#11/21/2023
#Use if/else to determine an employees pay

emp_name = input("Enter employee's name: ")
emp_hours = int(input("Enter nuber of hours worked: "))
emp_pay = float(input("Enter employee's pay rate: "))

print("------------------------------")

print("Employee name: ", emp_name)

#Calculations
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hours = 40

else:       #This represents if emp_hours is 40 or less
    ot_hours = 0
    reg_hours = emp_hours
#Calculate pay
ot_pay = (emp_pay * 1.5) * ot_hours
reg_pay = emp_pay *  reg_hours
gross_pay = ot_pay + reg_pay

#Display
print('Hours Worked  ', 'Pay Rate    ','OverTime    ','OverTime Pay    ', 'RegHour Pay     ', 'Gross Pay')
print('-----------------------------------------------------------------------------------------------')
print(f"{emp_hours:<15} {emp_pay:<15} {ot_hours:<15} {ot_pay:<15} {reg_pay:<15} {gross_pay:<15}")

    
                    
