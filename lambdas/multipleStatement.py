# second max element usung lambda
myList = [[1,2,3],[6,5,4]]

sortList = lambda x: (sorted(i) for i in x)

secondMax = lambda x, f:[y[len(y)-2] for y in f(x)]
a = secondMax(myList, sortList)
print(a)
