# anonymous function which has no name 
# "lambda" keyword is used for definition
# Syntax: lambda arguments: expression
# can be used with: filter(), map(), reduce()


# simple math calculation

a = lambda x, y, z : (x+y+z)/2
print(a(1,2,3))

# to reverse a string

str = "hello world"
reverse = lambda string: string[::-1]
print(reverse(str))