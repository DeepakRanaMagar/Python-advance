# matchobject: contains info about the search and match
import re 
txt = "hello, Goodmorning to the world"
a = re.search("dm",txt)
# print(a.group())
print(a.string)
# print(a.span())