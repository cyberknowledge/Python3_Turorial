def add(a,b):
	print(f"ADDING {a} + {b}")
	return a + b

def substract(a,b):
	print(f"SUBSTRACTING {a} - {b}")
	return a - b

def mutiply(a,b):
	print(f"MUTIPLYING {a} * {b}")
	return a * b

def divide(a,b):
	print(f"DIVIDING {a} / {b}")
	return a/b

print("Let's do some math with just function")

age=add(30,5)
hegiht = substract(78,4)
weight=mutiply(90,2)
iq=divide(100,2)

print(f"Age: {age}, Height: {hegiht}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in away
print("Here is a puzzle")

what = add(age,substract(hegiht,mutiply(weight,divide(iq,2))))

print("That becomes: ", what ,"Can you do it by hand?")

