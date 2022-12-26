# performs a repeatitive operation over the pair of the iterable

from functools import reduce
myList = [5, 6, 7, 8, 9, 10]
add = reduce((lambda x, y: x+y),myList)
print("The Sum is:",add)