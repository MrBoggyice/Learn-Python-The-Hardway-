# this import allows the use of argument variables
from sys import argv

# this takes two params which are script and input_file
script, input_file = argv


# this function takes in a file as a parameter and reads it
def print_all(f):
	print f.read()


# this function rewinds the file using seek built in function 
def rewind(f):
	f.seek(0)


# this function takes in two params 
def print_a_line(line_count, f):
	print line_count, f.readline()



# the current_file variable opens the input_file to be read from
current_file = open(input_file)


# this prints a string
print "First let's print the whole file: \n"

# the print_all function is called and the param is passed
print_all(current_file)

# this prints another bunch of string
print "Now let's rewind, kind of like a tape."

# the rewind function is called with the param passed
rewind(current_file)


# this prints a string
print "Let's print three lines:"

# the current_line holds 1 and the funciton is called with it
current_line = 1
print_a_line(current_line, current_file)


# the current_line is incremented by one and the funciton is called with it
current_line = current_line + 1
print_a_line(current_line, current_file)

# the current_line is incremented by one again and the funciton is called with it
current_line = current_line + 1
print_a_line(current_line, current_file)

read_data = current_file.read()

print len(read_data)
