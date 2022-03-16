# create a mapping of state to abbreviation
states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

# create a basic set of stages and some cities in them

cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-'*10)
print("Michigan's abrreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has : ", cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
	print(f"{state} is abrreviated {abbrev}")

# print every city in state
print('-'*10)
for abrrev, city in list(cities.items()):
	print(f"{abrrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abrrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-'*10)
#safely get a abbreviation by state that might not be there
state = states.get('Taxes')

if not state:
	print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX','Does Not Exist')
print(f"The city for the state 'TX' is {city}")
