# object that contains a countable number of values
# object can be iterated upon, meaning that you can traverse through all the value 
# consists of _iter_() and _next_() methods

# iterable objects/containers: Lists, tuples, dictionaries and sets 

a = ('car', 'planes', 'cycle', 'bikes')
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
