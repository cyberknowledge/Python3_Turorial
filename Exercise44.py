
''' Implicit Inheritance 
class Parent(object):
	def implicit(self):
		print("PARENT implicit()")

class Child(Parent):
	pass

dad  = Parent()
son = Child()

dad.implicit()
son.implicit()
'''
''' Override Explicitly
class Parent(object):
	def override(self):
		print("PARENT override()")

class Child(Parent):
	def override(self):
		print("Child override()")

dad  = Parent()
son = Child()

dad.override()
son.override() '''

''' Alter Before or After
class Parent(object):
	def altered(self):
		print("PARENT altered()")

class Child(Parent):
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered() # Call parent
		print("CHILD, AFTER PARENT altered()")

dad  = Parent()
son = Child()

dad.altered()
son.altered()
'''
''' Đa kế thừa 
class Parent(object):

	def override(self):
		print("PARENT override()")

	def implicit(self):
		print("Parent implicit()")

	def altered(self):
		print("PARENT altered()")

class Parent2(object):

	def override(self):
		print("PARENT2 override()")

	def implicit(self):
		print("Parent2 implicit()")

	def altered(self):
		print("PARENT2 altered()")

class Child(Parent,Parent2):

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		#super(Child, self).altered() # Call parent
		Parent2.altered(self)
		print("CHILD, AFTER PARENT altered()")

#dad = Parent()
son = Child()

#dad.implicit()
son.implicit()

#dad.override()
son.override()

#dad.altered()
son.altered()
'''

class Other(object):

	def override(self):
		print("Other override()")

	def implicit(self):
		print("Other implicit()")

	def altered(self):
		print("Other altered()")

class Child(object):
	
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print("Child override()")

	def altered(self):
		print("CHILD, BEFORE Other altered()")
		self.other.altered()
		print("CHILD, AFTER Other altered()")

son = Child()
son.implicit()
son.override()
son.altered()
		






