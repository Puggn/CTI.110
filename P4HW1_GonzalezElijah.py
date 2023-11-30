#Elijah Gonzalez
#11/16/2023
#Create a program to grade grades

from statistics import mean

#get number of grades from user
num_grades = int(input("How many grades will you enter? "))

#list code
grades_list = []

#Get grades from user
for i in range(num_grades):
    grade = float(input(f"Enter grade for Module {i + 1}: "))
    while grade < 0 or grade > 100:
      print("Invalid grade has been entered...")
      grade = float(input(f"Enter grade for Module {i + 1}: "))
    else:
        grades_list.append(grade)
print("-----------Results-----------")       
print(grades_list)
print("-----------Results-----------")  


min_grade = min(grades_list)
max_grade = max(grades_list)
sum_grade = sum(grades_list)
avg_grade = mean(grades_list)

print("Lowest Grade: ",f"{min_grade:.1f}")
print("Highest Grade",f"{max_grade:.1f}")
print("Sum of Grades:",f"{sum_grade:.1f}")
print("Lowest Grade:",f"{avg_grade:.1f}")


print("----------------------------------------")
