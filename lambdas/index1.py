def myfunc(n):
    return lambda a: a*n
doubler = myfunc(2)
print(doubler(10))