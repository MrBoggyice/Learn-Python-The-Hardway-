from sys import argv

script, filename = argv

text = open(filename, 'w+')

line1 = raw_input("first line please>>")
line2 = raw_input("second line please>>")
line3 = raw_input("And finally the third line please>>")

print "Now I wanna stuff into %r " % filename
readT = text.write("%s \n %s \n %s" % (line1, line2, line3))

readT = open(readT, 'r')

print "now i'm going to read this %r" % filename
print readT.read()

print "and finally i'm closing"
text.close()