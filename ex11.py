print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
	
# get a number from someone to do math
# ex) x = int(raw_input()) - which gets the number as a string from raw_input() then converts it to an integer using int().
# difference between input and raw_input
# - input () function will try to convert things you enter as if they were python code, but it has security problems so you should avoid it
#
