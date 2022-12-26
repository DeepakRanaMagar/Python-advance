# using lambdas with list
list = [lambda arg = x: arg * 10 for x in range(1,5)]

for a in list:
    print(a())