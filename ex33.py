numbers = []
testvar = 17


def myfunc(incr_by):
	i = 0
	while i < testvar:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + incr_by
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num

#myfunc(5)

for i in range(testvar):
	numbers.append(i)
	print numbers