cars = 100 # says there are 100 cars
space_in_a_car = 4.0 # says there's just 4.0 spaces in each car
drivers = 30 # there are 30 drivers
passengers = 90 # there are 90 passengers
cars_not_driven = cars - drivers # subtracts drivers from number of cars
cars_driven = drivers # cars driven equals drivers
carpool_capacity = cars_driven * space_in_a_car # capacitpy is the driven cars multiplied by car space
average_passengers_per_car = passengers / cars_driven

""" This prints the string along with each of the varables above """

print "There are", cars, " cars available."
print "There are only ", drivers, " drivers available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can Transport ", carpool_capacity, " people today."
print "We have ", passengers, " to carpool today."
print "We need to put about ", average_passengers_per_car, " in each car."