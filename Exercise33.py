#i = 0
#numbers = []

#while i < 6:
#	print(f"At the top i is {i}")
#	numbers.append(i)

#	i = i + 1
#	print("numbers now: ",numbers)
#	print(f"At the bottom i is {i}")


#print("The numbers: ")
#for num in numbers:
#	print(num)
def Exe33(x):
	i = 0
	numbers = []
	while i < x :
		print(f"At the top i is {i}")
		numbers.append(i)
		i=i+1
		print("numbers now: ",numbers)
		print(f"At the bottom i is {i}")
x = int(input("X => "))
Exe33(x)
print("Well done")