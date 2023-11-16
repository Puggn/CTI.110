#Elijah Gonzalez
#11/16/2023
#Create a program to grade grades

from statistics import mean

#Enter Grades

grade_m1 = float(input("Enter grade for Module 1: "))
grade_m2 = float(input("Enter grade for Module 2: "))
grade_m3 = float(input("Enter grade for Module 3: "))
grade_m4 = float(input("Enter grade for Module 4: "))
grade_m5 = float(input("Enter grade for Module 5: "))
grade_m6 = float(input("Enter grade for Module 6: "))

#list code
grades_list = []
#adding value to list
grades_list.append(grade_m1)
grades_list.append(grade_m2)
grades_list.append(grade_m3)
grades_list.append(grade_m4)
grades_list.append(grade_m5)
grades_list.append(grade_m6)

#Results table
print("------------Results------------")

min_grade = min(grades_list)
max_grade = max(grades_list)
sum_grade = sum(grades_list)
avg_grade = mean(grades_list)

print("Lowest Grade: ",f"{min_grade:.1f}")
print("Highest Grade",f"{max_grade:.1f}")
print("Sum of Grades:",f"{sum_grade:.1f}")
print("Lowest Grade:",f"{avg_grade:.1f}")


print("----------------------------------------")
