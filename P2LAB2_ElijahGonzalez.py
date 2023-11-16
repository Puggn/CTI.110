#Elijah Gonzalez
#11/16/2023
#Calculateds decimal values

from statistics import mean

#gets input
num1 = float(input("Enter a decimal value: "))
num2 = float(input("Enter a decimal value: "))
num3 = float(input("Enter a decimal value: "))
num4 = float(input("Enter a decimal value: "))

#creates empty list
num_list =[]

#Add values to list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)

print(num_list)

#Call methouds on the list to calculate for the product
list_sum = sum(num_list)
list_avg = mean(num_list)

#Output to user formatted with f-string
print(f"(list_sum:.0f) {list_avg:.0f}")
print(f"(list_sum:.3f) {list_avg:.3f}")
