# sub: replace matches with the string of choice

#  \s returns match where the string contains whitespace
# 
import re
txt = "Hello world, Goodmorning"
a = re.sub("\s","0",txt, 2)
print(a)