# cheese_and_cracker function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses !")
	print(f"You have {boxes_of_crackers} boxes_of_crackers !")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

# argument is number
print("We can just give the function numbers directly: ")
cheese_and_crackers(20,30)

# argiment is variable
print("OR, we can use variable from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# argument is math 
print("We can even do math inside too: ")
cheese_and_crackers(10+20,5+6)

# argument combine between variable and number
print("And we can combine the two, variable and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
