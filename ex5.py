my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." %my_weight
print "Actually that's not that heavy."
print "He's got %s eyes and %s hiar" %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# notes
# %s, %r and %d - these are formatters, they tell python to take the variable on the right and put it in to replace the % with its value.
# rounding a floating point number - use the "round()" function like this - round(1.7333) 
# 