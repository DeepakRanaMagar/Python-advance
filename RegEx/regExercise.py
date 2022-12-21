# regEx: Regular expression, sequence of characters that forms  a search pattern
# Checks if the the string contains specfic search pattern 
# re -package is used to work with regEx
import re

txt = "Hello, Good morning world"
x = re.search("^Hello.*world$", txt)
print(x)

# functions : findall, search, split, sub 