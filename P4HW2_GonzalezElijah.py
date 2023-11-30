#CTI-110
#P3HW2 - Salary
#Elijah Gonzalez
#11/21/2023
#Use if/else to determine an employees pay

#create varables to hold totals paid to employees
num_em = 0
total_reg = 0
total_ot = 0
total_gross = 0

emp_name = input("Enter employee's name or type Done to quit: ")
while emp_name != "Done":
    num_em += 1
    emp_hours = int(input("Enter number of hours worked: "))
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
    total_ot += ot_pay
    reg_pay = emp_pay *  reg_hours
    total_reg += reg_pay
    gross_pay = ot_pay + reg_pay
    total_gross += gross_pay

    #Display
    print('Hours Worked  ', 'Pay Rate    ','OverTime    ','OverTime Pay    ', 'RegHour Pay     ', 'Gross Pay')
    print('-----------------------------------------------------------------------------------------------')
    print(f"{emp_hours:<15} {emp_pay:<15} {ot_hours:<15} {ot_pay:<15} {reg_pay:<15} {gross_pay:<15}")
    emp_name = input("Enter Employee name or Done to terminate: ")
#This code executes after looks breaks
print("Done adding Employees")

print(f"Total number of employees entered: {num_em}")
print(f"Total amount paid for overtime: {ot_pay}")
print(f"Total amount paid for regualr hours: {reg_pay}")
print(f"Total amount paid in gross: {total_gross}")
