class Animal(object):
	pass

# Dog is a animal, has a name 
class Dog(Animal):
	def __init__(self, name):
		self.name = name

# Cat is a animal, has a name
class Cat(Animal):
	def __init__(self, name):
		self.name = name

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None

# Employee is a person , has a name, a pet and an salary
class Employee(Person):
	def __init__(self, name, salary):
		# call Person
		super(Employee, self).__init__(name) # Person.__init__(name) or super().__init__(name)
		self.salary = salary

class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

## rover is a Dog
rover = Dog("Rover")

# satan is a cat
satan = Cat("Satan")

# mary is a person
mary = Person("Mary")
# mary gas a pet - satan
mary.pet = satan

# frank is Employee, has  a salary and has a pet - rover
frank = Employee("Frank", 120000)
frank.pet = rover

# flipper is a fish
flipper = Fish()

#cruouse is a salmon
crouse = Salmon()

# harry is a halbut
harry = Halibut()