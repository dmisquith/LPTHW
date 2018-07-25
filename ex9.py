# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """ 
There's something going on here.
With the three  double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#What if I wanted to start the months on a new line?
# - you would start the string with \n
# ex) \nJan\nFeb\nMar\nApr\nJun\nJul\nAug 

#Why do the  \n  newlines not work when I use %r?
# - thats just how %r formatting works; it prints it the way you wrote it, its the "raw" format for debugging

# the \ (backslash) character is a way we can put difficult-to-type characters into a string 

