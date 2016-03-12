# this variable x holds a string and a formatter with a value of 10
x = "There are %d types of people. " % 10

# this variable binary just holds an ordinary string
binary = "binary"

# this varible as well holds an ordinary string as well
do_not = "don't"

# the variable y holds a string and formatters which has a value of two variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x and y
print x
print y

# prints a string and a formatter with a value of variable x
print "I said: %r. " % x
# prints a string and a formatter with a value of variable x
print "I also said: '%s'." % y

hilarious = False
n_hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r."

print joke_evaluation % hilarious
print joke_evaluation % n_hilarious

w = "This is the left side of..."
e = "a string with a right side."

# this concatenates the variables w and e into one long string
print w + e