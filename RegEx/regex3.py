# split: returns a list containing splitted string at end match 
# maxsplit: parameter specifies the num of occurrences
import re 

txt = "Hello world, Goodmorning"
a = re.split("\s", txt, maxsplit=1)
print(a)