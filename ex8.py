formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# %s and %r are used for getting debugging information about something
# - the %r will give you the "raw programmer's" version of the variable
# python recognizes True and False as keywords representing the concept of true and false
# python is going to print the strings in the most efficient way possible, not replicate exactly the way you wrote them 
# 	ex) %r will sometimes print things with single-quotes when I wrote them in double quotes
# 