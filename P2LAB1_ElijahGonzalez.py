#Elijah Gonzalez
#11/16/2023
#Calculates Car Milage and Gas prices for your Journey

#User Input
mpg = float(input("Enter car gas milage: "))
cpg = float(input("Enter cost per gallon: "))
#calc cost 20 miles
mile_cost_20 = (20/mpg)*cpg
#calc cost 75 miles
mile_cost_75 = (75/mpg)*cpg
#calc cost 500 miles
mile_cost_500 = (500/mpg)*cpg
#Display Out come
print(f"Cost for 20 mile: {mile_cost_20:.2f}")
print(f"Cost for 75 mile: {mile_cost_75:.2f}")
print(f"Cost for 500 mile: {mile_cost_500:.2f}")
