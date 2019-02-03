"""
CSC 221
M1HW2
Brian Schweikart
2/3/19
Goal: Gold
"""

# Question 1
name = input("What is the product name?: ")
price = int(input("What is the cost?: "))
number_Units = int(input("How many?: "))

sub_Total = price * number_Units
tax_State = 0.04
tax_County = 0.02
total = sub_Total + (sub_Total * tax_State) + (sub_Total * tax_County)
print("SubTotal: $",sub_Total)
print("Total: $",total)
# Question 2


# Question 3
	# see other file